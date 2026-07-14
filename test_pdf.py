from utils.pdf_generator import create_pdf

dummy_report = """
Executive Summary

This is a sample report generated for testing the PDF layout.

Key Insights

• Sales increased by 15%.
• Product Line A performed the best.
• Customer retention improved.

Recommendations

• Increase inventory for top-performing products.
• Focus marketing efforts on high-value customers.
"""

create_pdf(
    output_path="reports/test_report.pdf",
    report_text=dummy_report,
    chart_path="figures/chart.png"
)

print("PDF Generated Successfully!")