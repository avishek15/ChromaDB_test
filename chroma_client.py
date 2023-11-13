import chromadb
from chromadb.utils import embedding_functions
from PyPDF2 import PdfReader
from tqdm import tqdm


pdf_path = r"C:\Documents\Trading-Volatility.pdf"
reader = PdfReader(pdf_path)
# page = reader.pages[100]
# print(type(page.extract_text()))

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="paraphrase-albert-small-v2")
client = chromadb.PersistentClient(path="./docs_cache/")


collection = client.get_or_create_collection(name="pdf_books", embedding_function=sentence_transformer_ef)
doc_list = []
metadata_list = []
id_list = []

for pageno, page in tqdm(enumerate(reader.pages)):
	doc_list.append(page.extract_text())
	metadata_list.append({"reference": "Trading_Volatility_{pageno + 1}"})
	id_list.append(str(pageno))

collection.add(documents=doc_list,
	metadatas=metadata_list,
	ids=id_list)

print(collection.count())
