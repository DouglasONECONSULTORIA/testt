from typing_extensions import List, TypedDict
from langchain_core.documents import Document
from langchain_core.prompts.chat import ChatPromptTemplate
import sys, os
from ..ingestion.vector_store import vector_store


class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    return {"context": retrieved_docs}
