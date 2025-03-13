from langchain.tools.retriever import create_retriever_tool
from langchain_core.tools.simple import Tool
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


def _retriever_tool(collection_name: str = "rag_agent_collection") -> Tool:
    vectorstore = Chroma(
        collection_name=collection_name,
        embedding_function=OllamaEmbeddings(model="llama3:latest"),
    )
    retriever = vectorstore.as_retriever()

    retriever_tool = create_retriever_tool(
        retriever,
        "retrieve_infos",
        "Search and return information",
    )
    return retriever_tool


retriever_tool = _retriever_tool()
