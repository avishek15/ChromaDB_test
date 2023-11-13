import chromadb
from chromadb.utils import embedding_functions

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="paraphrase-albert-small-v2")
client = chromadb.PersistentClient(path="./docs_cache/")


collection = client.get_or_create_collection(name="pdf_books", embedding_function=sentence_transformer_ef)

query = "What is a class?"

fetched_results = collection.query(query_texts=[query], n_results=3)

# The data structure of the returned result is a dictionary, with lists. We fetch the distance
# and the documents. Then we select the matches for the first query (since we only have one
# query, this list of length 1). Then we iterate through the 3 results.
for dist, doc in zip(fetched_results['distances'][0], fetched_results['documents'][0]):
    print(f"DISTANCE: {dist}\n{doc}")
    print('=' * 25)
