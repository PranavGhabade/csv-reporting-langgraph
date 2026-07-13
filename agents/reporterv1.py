import json
import os

from llm import llm
from state import GraphState
from prompts.reporter_prompt import REPORTER_PROMPT

def reporter_node(state: GraphState):

    print("\n===== REPORTER NODE =====")

    dataset_info = json.dumps(
        state["profile"]["dataset_info"],
        indent=2,
        default=str
    )

    analysis_results = json.dumps(
        state["analysis_results"],
        indent=2,
        default=str
    )

    prompt = REPORTER_PROMPT.format(
        dataset_info=dataset_info,
        summary=state["analysis_plan"]["summary"],
        analysis_results=analysis_results
    )

    response = llm.invoke(prompt)

    report = response.content[0]["text"]

    if state.get("chart_path"):

        report += f"\n\n## Visualization\n\n![Chart]({state['chart_path']})\n"

    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/report.md",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print("Report Saved: reports/report.md")

    return {

        "report_markdown": report

    }