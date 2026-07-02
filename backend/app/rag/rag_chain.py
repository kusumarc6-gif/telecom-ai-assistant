import os
from dotenv import load_dotenv

from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

from app.rag.retriever import get_retriever

load_dotenv()


def get_rag_chain():

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0
    )

    retriever = get_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )

    return qa_chain