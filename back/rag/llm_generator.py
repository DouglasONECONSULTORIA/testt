from langchain.chat_models import init_chat_model
from langgraph.graph import START, StateGraph
from langchain_core.prompts.chat import ChatPromptTemplate
from .retrieval.retriever import State, retrieve
from .ingestion.vector_store import vector_store


# llm = init_chat_model("gpt-4o-mini", model_provider="openai")
llm = init_chat_model("llama3-8b-8192", model_provider="groq")

prompt = ChatPromptTemplate.from_template(
    """
    Você é um assistente para tarefas de perguntas e respostas de um hortifrut. 
    Use os seguintes trechos de contexto recuperados para responder à pergunta. 
    Se você não souber a resposta, apenas diga que não sabe.
    Use no máximo três frases e mantenha a resposta concisa.
    \nPergunta: {question} \nContexto: {context} \nResposta:"""
)

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    messages = prompt.invoke({"question": state["question"], "context": docs_content})
    response = llm.invoke(messages)
    return {"answer": response.content}


graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")

graph = graph_builder.compile()
