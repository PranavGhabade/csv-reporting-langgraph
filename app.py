from graph import graph
from state import GraphState


state = GraphState(

    csv_path="sample_data/test.csv",

    user_prompt="""
Generate a professional data analysis report.
"""
)

result = graph.invoke(state)

print(result["report_markdown"])

print("\nPDF Generated Successfully")
print(result["pdf_path"])