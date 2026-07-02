from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.rag_chain import get_rag_chain

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
def chat(request: ChatRequest):

    qa_chain = get_rag_chain()

    response = qa_chain.invoke(
        {"query": request.question}
    )

    return {
        "answer": response["result"],
        "sources": [
            doc.metadata
            for doc in response["source_documents"]
        ]
    }
