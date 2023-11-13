# This is a simple demonstration of how vector databases work


You will need to first install the requirements. We are using:
- Chroma for VectorDB
- Sentence Transformers for document embedding

There is a Python book, by the author Dave Kuhlman, provided to experiment.

You can also download it from his domain: https://www.davekuhlman.org/python_book_01.pdf

To run the experiment, run chroma_client to vectorize each page and store them in the DB.

Then run the chroma_request to fetch relevant pages from the DB.
