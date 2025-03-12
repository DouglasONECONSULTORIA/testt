from langchain_core.vectorstores import InMemoryVectorStore
from .embeddings import embeddings
from .document_loader import all_splits

vector_store = InMemoryVectorStore(embeddings)

_ = vector_store.add_documents(documents=all_splits)