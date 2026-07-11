import os
import streamlit as st

from graph import graph
from state import GraphState


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="AI CSV Reporting System",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# Header
# ==========================================================

st.title("📊 AI CSV Reporting System")

st.markdown(
    """
Generate automated data analysis reports from **any CSV dataset**
using **LangGraph, Google Gemini, Pandas and Matplotlib**.
"""
)

# ==========================================================
# Metrics
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Framework", "LangGraph")

with col2:
    st.metric("LLM", "Gemini")

with col3:
    st.metric("Charts", "Matplotlib")

with col4:
    st.metric("Reports", "Markdown")

st.divider()

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.header("Workflow")

    st.success("1. Upload CSV")

    st.success("2. Profiler")

    st.success("3. Planner")

    st.success("4. Analyst")

    st.success("5. Visualizer")

    st.success("6. Reporter")

    st.divider()

    st.info(
        """
Leave **Analysis Instructions** empty for a completely
automatic report.
"""
    )

# ==========================================================
# Upload CSV
# ==========================================================

uploaded_file = st.file_uploader(
    "📁 Upload CSV File",
    type=["csv"]
)

# ==========================================================
# User Prompt
# ==========================================================

user_prompt = st.text_area(

    "Analysis Instructions (Optional)",

    placeholder="""
Examples

• Analyze customer behaviour.

• Identify important trends.

• Focus on sales performance.

• Generate an executive summary.

• Provide recommendations.
""",

    height=170

)

# ==========================================================
# Generate Button
# ==========================================================

if st.button("🚀 Generate Report", use_container_width=True):

    if uploaded_file is None:

        st.warning("Please upload a CSV file.")

    else:

        if not user_prompt.strip():

            user_prompt = """
Generate a professional data analysis report.

Identify the important insights.

Generate one meaningful visualization.

Provide useful recommendations.
"""

        os.makedirs("temp", exist_ok=True)

        csv_path = os.path.join(
            "temp",
            uploaded_file.name
        )

        with open(csv_path, "wb") as file:

            file.write(uploaded_file.getbuffer())

        state = GraphState(

            csv_path=csv_path,

            user_prompt=user_prompt

        )

        progress = st.progress(0)

        status = st.empty()

        status.write("📂 Loading dataset...")
        progress.progress(10)

        try:

            with st.spinner("Running LangGraph Workflow..."):

                result = graph.invoke(state)

            progress.progress(100)

            status.success("✅ Report Generated Successfully!")

        except Exception as e:

            st.error(e)

            st.stop()

        st.divider()

        # ==================================================
        # Tabs
        # ==================================================

        tab1, tab2 = st.tabs(

            [

                "📈 Visualization",

                "📄 Report"

            ]

        )

        # ==================================================
        # Visualization
        # ==================================================

        with tab1:

            if result.get("chart_path"):

                st.image(

                    result["chart_path"],

                    caption="Generated Visualization",

                    use_container_width=True

                )

            else:

                st.info("No visualization generated.")

        # ==================================================
        # Report
        # ==================================================

        with tab2:

            st.markdown(result["report_markdown"])

            st.download_button(

                label="⬇ Download Markdown Report",

                data=result["report_markdown"],

                file_name="report.md",

                mime="text/markdown",

                use_container_width=True

            )

        st.balloons()