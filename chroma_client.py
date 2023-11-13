import chromadb
from chromadb.utils import embedding_functions
from PyPDF2 import PdfReader
import unicodedata
from tqdm import tqdm

pdf_path = "./python_book_01.pdf"
reader = PdfReader(pdf_path)
# page = reader.pages[100]
# print(type(page.extract_text()))

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="paraphrase-albert-small-v2")
client = chromadb.PersistentClient(path="./docs_cache/")

collection = client.get_or_create_collection(name="pdf_books", embedding_function=sentence_transformer_ef)
doc_list = []
metadata_list = []
id_list = []

for pageno, page in tqdm(enumerate(reader.pages)):
    # This is required to normalize the text to unicode data
    new_str = unicodedata.normalize("NFKD", page.extract_text())
    doc_list.append(new_str)
    metadata_list.append({"reference": f"python_{pageno + 1}"})
    id_list.append(str(pageno))

print(f"Adding {len(doc_list)} to the collection.")
collection.add(documents=doc_list,
               metadatas=metadata_list,
               ids=id_list)

print(f"There are {collection.count()} documents in the collection.")
