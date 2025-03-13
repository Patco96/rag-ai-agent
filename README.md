# RAG AI Agent

A Retrieval Augmented Generation system using vector databases to enhance LLM responses with relevant context.

## Overview

This project:

- Stores document data in ChromaDB
- Retrieves context based on user queries
- Augments LLM responses with retrieved information

## Installation

Install the package with Poetry:

```bash
# Clone the repository
git clone https://github.com/yourusername/rag-ai-agent.git
cd rag-ai-agent

# Install the package
poetry install
```

Or install in development mode:

```bash
poetry install -e .
```

## Usage

After installation, you can use the package:

```python
# Initialize the data
from rag_ai_agent.data import initialize_data
initialize_data.setup()

# Run the agent
from rag_ai_agent.agent import run
run.start_agent()
```

You can also use the CLI commands:

```bash
# Activate Poetry environment
poetry shell

# Initialize data
rag-init

# Run the agent
rag-agent
```

## Customization

- **Custom Datasets**:

```python
from rag_ai_agent.data import initialize_data
from your_dataset import CustomDataset

initialize_data.setup(dataset=CustomDataset)
```

- **Custom Embeddings**:

```python
from rag_ai_agent.embeddings import get_embedding_function
custom_embeddings = get_embedding_function(model_name="your-model-name")
```

- **Custom LLM**: Modify the LLM configuration in `rag_ai_agent.config`
