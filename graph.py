from langgraph.graph import StateGraph, START, END

from state import GraphState

from agents.profiler import profiler_node
from agents.planner import planner_node
from agents.analyst import analyst_node
from agents.visualizer import visualizer_node
from agents.reporter import reporter_node


builder = StateGraph(GraphState)

builder.add_node("Profiler", profiler_node)
builder.add_node("Planner", planner_node)
builder.add_node("Analyst", analyst_node)
builder.add_node("Visualizer", visualizer_node)
builder.add_node("Reporter", reporter_node)


builder.add_edge(START, "Profiler")

builder.add_edge("Profiler", "Planner")

builder.add_edge("Planner", "Analyst")

builder.add_edge("Analyst", "Visualizer")

builder.add_edge("Visualizer", "Reporter")

builder.add_edge("Reporter", END)


graph = builder.compile()