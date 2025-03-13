# %%
import chromadb
from chromadb.utils import embedding_functions
from chroma_datasets import SciQ
from chroma_datasets.utils import import_into_chroma

# Initialize the Chroma client
chroma_client = chromadb.Client()

# Initialize the embedding function
embedding_function = embedding_functions.DefaultEmbeddingFunction()

# Import the SciQ dataset into Chroma
collection = import_into_chroma(
    chroma_client=chroma_client,
    dataset=SciQ,
    embedding_function=embedding_function,
    collection_name="rag_agent_collection",
)

# Verify that the data is loaded (commented out for now)
# result = collection.query(query_texts=["What's a meteorite?"], n_results=1)
# print(result)
# %%

collection = chroma_client.get_collection("rag_agent_collection")

# %%
