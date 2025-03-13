# RAG AI Agent

A Retrieval Augmented Generation system using vector databases to enhance LLM responses with relevant context, based on [LangGraph's guide](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/).

## Overview

This project:

- Stores document data in ChromaDB
- Retrieves context based on user queries
- Augments LLM responses with retrieved information

## Installation

Clone and install the package with Poetry:

```bash
git clone https://github.com/yourusername/rag-ai-agent.git
cd rag-ai-agent
python -m venv .venv
source .venv/bin/activate
poetry install
```

## Usage

After installation, you can initialize the data:

```bash
python initialize_data.py
```

Then, implement the graph on `src/graph.py` and run the agent:

```bash
python run.py
```
