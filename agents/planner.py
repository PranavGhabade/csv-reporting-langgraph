import json

from llm import llm
from state import GraphState
from prompts.planner_prompt import PLANNER_PROMPT

def planner_node(state: GraphState):

    print("\n===== PLANNER NODE =====")

    prompt = PLANNER_PROMPT.format(

        dataset_info=state["profile"]["dataset_info"],

        schema=state["profile"]["schema"],

        column_groups=state["profile"]["column_groups"],

        data_quality=state["profile"]["data_quality"],

        user_prompt=state["user_prompt"]

    )

    response = llm.invoke(prompt)

    json_text = response.content[0]["text"]

    print("\n===== JSON RESPONSE =====")
    print(json_text)

    plan = json.loads(json_text)

    print("\nPlanning Complete.")

    return {

        "analysis_plan": plan

    }