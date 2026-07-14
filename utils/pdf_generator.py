import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

styles = getSampleStyleSheet()


def clean_report(text):
    """
    Remove basic markdown symbols so the PDF looks cleaner.
    """

    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    text = text.replace("**", "")
    text = text.replace("* ", "• ")
    text = text.replace("```", "")

    return text


def add_header_footer(canvas, doc):

    width, height = doc.pagesize

    canvas.setStrokeColor(colors.grey)

    canvas.line(40, height - 70, width - 40, height - 70)

    canvas.line(40, 45, width - 40, 45)

    canvas.setFont("Helvetica", 9)

    canvas.drawString(
        40,
        30,
        "ABC Analytics Pvt Ltd"
    )

    canvas.drawCentredString(
        width / 2,
        30,
        "Confidential"
    )

    canvas.drawRightString(
        width - 40,
        30,
        f"Page {doc.page}"
    )


def create_pdf(

    output_path,
    report_text,
    chart_path

):

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    doc = SimpleDocTemplate(

        output_path,

        topMargin=0.15 * inch,
        bottomMargin=0.7 * inch,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch

    )

    story = []

    logo_path = "assets/logo.png"

    logo = ""

    if os.path.exists(logo_path):

        logo = Image(

            logo_path,

            width=0.6 * inch,
            height=0.6 * inch

        )

    company = Paragraph(

        """
        <font size=18><b>ABC Analytics Pvt Ltd</b></font><br/>
        <font size=10 color='grey'>
        Data Driven Decisions with AI
        </font>
        """,

        styles["Normal"]

    )

    header = Table(

        [

            [logo, company]

        ],

        colWidths=[1.0 * inch, 5.7 * inch]

    )

    header.setStyle(

        TableStyle(

            [

                ("VALIGN", (0, 0), (-1, -1), "TOP"),

                ("LEFTPADDING", (0, 0), (-1, -1), 0),

                ("RIGHTPADDING", (0, 0), (-1, -1), 0),

                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),

            ]

        )

    )

    story.append(header)

    story.append(Spacer(1, 0.20 * inch))

    title = styles["Heading1"]

    title.alignment = TA_CENTER

    story.append(

        Paragraph(

            "AI GENERATED DATA ANALYSIS REPORT",

            title

        )

    )

    story.append(

        Spacer(

            1,

            0.20 * inch

        )

    )

    if chart_path and os.path.exists(chart_path):

        chart = Image(

            chart_path,

            width=6.3 * inch,
            height=3.4 * inch

        )

        chart.hAlign = "CENTER"

        story.append(chart)

        story.append(

            Spacer(

                1,

                0.25 * inch

            )

        )

    report_text = clean_report(report_text)

    body = styles["BodyText"]

    body.leading = 18

    body.spaceAfter = 8

    story.append(

        Paragraph(

            report_text.replace("\n", "<br/>"),

            body

        )

    )

    doc.build(

        story,

        onFirstPage=add_header_footer,

        onLaterPages=add_header_footer

    )