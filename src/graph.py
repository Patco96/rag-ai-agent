from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import ToolNode

from src.agent import AgentState
from src.nodes import agent, generate, rewrite
from src.retriever import retriever_tool
from src.edges import tools_condition, grade_documents

# Define a new graph

workflow = StateGraph(AgentState)

# Define the nodes we will cycle between
workflow.add_node("agent", agent)
retrieve = ToolNode([retriever_tool])
workflow.add_node("retrieve", retrieve)
workflow.add_node("rewrite", rewrite)
workflow.add_node("generate", generate)

# Call agent node to decide to retrieve or not
workflow.add_edge(START, "agent")

# Decide whether to retrieve
workflow.add_conditional_edges(
    "agent",
    tools_condition,
    {"tools": "retrieve", END: END},
)

# Edges taken after the `action` node is called.
workflow.add_conditional_edges("retrieve", grade_documents)
workflow.add_edge("generate", END)
workflow.add_edge("rewrite", "agent")

# Compile
graph = workflow.compile()
