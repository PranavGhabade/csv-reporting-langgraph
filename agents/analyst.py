from llm import llm
from state import GraphState

from prompts.analyst_prompt import ANALYST_PROMPT
from utils.executor import execute_code


def analyst_node(state: GraphState):

    print("\n===== ANALYST NODE =====")

    prompt = ANALYST_PROMPT.format(

        schema=state["profile"]["schema"],

        column_groups=state["profile"]["column_groups"],

        tasks=state["analysis_plan"]["tasks"]

    )

    response = llm.invoke(prompt)

    code = response.content[0]["text"]

    print("\n===== GENERATED ANALYSIS CODE =====\n")
    print(code)

    results = execute_code(
        code,
        state["dataframe"]
    )

    print("\n===== ANALYSIS RESULTS =====\n")
    print(results)

    return {

        "analysis_results": results

    }