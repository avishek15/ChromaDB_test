# ChromaDB Test — Vector Database Examples

**Practical examples for using ChromaDB in RAG applications.**

## What It Does

A collection of Jupyter notebooks and scripts demonstrating ChromaDB usage for semantic search and RAG (Retrieval-Augmented Generation).

**Why it matters:** ChromaDB is powerful but documentation is scattered. This gives you working examples.

## Quick Start

\`\`\`bash
# Clone
git clone https://github.com/avishek15/ChromaDB_test.git
cd ChromaDB_test

# Install
pip install -r requirements.txt

# Run notebooks
jupyter notebook
\`\`\`

## Examples Included

| Notebook | What You Learn |
|----------|----------------|
| `01_basics.ipynb` | CRUD operations |
| `02_embeddings.ipynb` | Working with embeddings |
| `03_semantic_search.ipynb` | Building search |
| `04_rag_pipeline.ipynb` | Full RAG implementation |

## Tech Stack

- **Python 3.10+**
- **ChromaDB** — Vector database
- **OpenAI** — Embeddings
- **LangChain** — LLM orchestration

## Key Concepts

\`\`\`python
# Add documents
collection.add(
    documents=["This is doc 1", "This is doc 2"],
    metadatas=[{"source": "a"}, {"source": "b"}],
    ids=["id1", "id2"]
)

# Query
results = collection.query(
    query_texts=["search query"],
    n_results=5
)
\`\`\`

## License

MIT License - see [LICENSE](LICENSE)

## Author

Built by [Avishek Majumder](https://invaritech.ai)
