from typing import TypedDict, Any

import pandas as pd

class GraphState(TypedDict):

    csv_path: str

    user_prompt: str

    dataframe: Any

    profile: dict

    analysis_plan: dict

    analysis_results: dict

    report_markdown: str