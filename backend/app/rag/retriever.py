from langchain_community.vectorstores import FAISS
from app.rag.embeddings import get_embedding_model


def get_retriever():
    embedding_model = get_embedding_model()

    vector_db = FAISS.load_local(
        "faiss_index",
        embedding_model,
        allow_dangerous_deserialization=True
    )

    # Retrieve more relevant documents for better answers
    retriever = vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 10
        }
    )

    return retriever