from fastapi import FastAPI
from pydantic import BaseModel
import dotenv,getpass,os
from rag.llm_generator import graph



dotenv.load_dotenv(override=True)

app = FastAPI()


@app.get("/")
def rag_question(question: str) -> dict:
    response = graph.invoke({"question": question})
    
    return response["answer"]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
