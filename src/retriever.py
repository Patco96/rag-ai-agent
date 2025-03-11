import chromadb
chroma_client = chromadb.Client()


class Retriever:
    def __init__(self, collection_name: str="rag_agent_collection"):
        self.client =  chromadb.Client()
        self.collection = chroma_client[collection_name]

    def query(self, queries: list[str], n_results: int=1):
        return self.collection.query_texts(query=queries, n_results=n_results)