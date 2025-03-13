from langchain.tools.retriever import create_retriever_tool
from langchain_core.tools.simple import Tool
from langchain_chroma import Chroma
from chromadb.utils import embedding_functions


def _retriever_tool(collection_name: str = "rag-chroma-sciq") -> Tool:
    embedding_function = embedding_functions.DefaultEmbeddingFunction()

    vectorstore = Chroma(
        collection_name=collection_name,
        embedding_function=embedding_function,
    )
    retriever = vectorstore.as_retriever()

    retriever_tool = create_retriever_tool(
        retriever,
        "retrieve_infos",
        "Search and return information",
    )
    return retriever_tool


retriever_tool = _retriever_tool()


# Check that the retriever tool is working (commented out for now)
# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model="llama3.1", streaming=True, temperature=0)
# llm.bind_tools([retriever_tool])
# response = llm.invoke("What are the most common seedless vascular plants?")
# print(response.content)
