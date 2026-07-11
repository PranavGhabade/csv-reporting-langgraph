import os
import matplotlib.pyplot as plt

from state import GraphState


def visualizer_node(state: GraphState):

    print("\n===== VISUALIZER NODE =====")

    df = state["dataframe"]

    print(state["analysis_plan"]["charts"])

    chart = state["analysis_plan"]["charts"][0]

    print(chart)

    chart_request = str(chart).lower()

    os.makedirs("figures", exist_ok=True)

    chart_path = "figures/chart.png"

    try:

        x_col = chart["x_column"]
        y_col = chart["y_column"]
        chart_type = chart["chart_type"]
        aggregation = chart["aggregation"]

        if aggregation == "sum":
            plot_data = df.groupby(x_col)[y_col].sum()

        elif aggregation == "mean":
            plot_data = df.groupby(x_col)[y_col].mean()

        elif aggregation == "count":
            plot_data = df.groupby(x_col)[y_col].count()

        else:
            plot_data = df.groupby(x_col)[y_col].sum()

        plt.figure(figsize=(10, 6))

        if chart_type == "line":
            plot_data.plot(kind="line")

        elif chart_type == "pie":
            plot_data.plot(kind="pie", autopct="%1.1f%%")

        else:
            plot_data.plot(kind="bar")

        plt.title(chart["title"])

        plt.tight_layout()

        plt.savefig(chart_path)

        plt.close()

        print("Chart Saved:", chart_path)

        plt.title(state["analysis_plan"]["charts"][0])

        plt.tight_layout()

        plt.savefig(chart_path)

        plt.close()

        print("Chart Saved:", chart_path)

    except Exception as e:

        print(e)

        chart_path = None

    return {

        "chart_path": chart_path

    }