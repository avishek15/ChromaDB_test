import chromadb
from chromadb.utils import embedding_functions

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="paraphrase-albert-small-v2")
client = chromadb.PersistentClient(path="./docs_cache/")


collection = client.get_or_create_collection(name="pdf_books", embedding_function=sentence_transformer_ef)

print(collection.peek())
query = "What is Call options?"

fetched_results = collection.query(query_texts=[query], n_results=3)


print(fetched_results)

