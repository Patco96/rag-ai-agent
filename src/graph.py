from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import ToolNode

from src.agent import AgentState
from src.nodes import agent, generate, rewrite
from src.retriever import retriever_tool
from src.edges import tools_condition, grade_documents

# Define a new graph

workflow = StateGraph(AgentState)

# Define the nodes we will cycle between
...

# Call agent node to decide to retrieve or not
...

# Decide whether to retrieve
...

# Edges taken after the `action` node is called.
...

# Compile

graph = workflow.compile()
