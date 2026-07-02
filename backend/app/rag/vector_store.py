from langchain_community.vectorstores import FAISS
from app.rag.embeddings import get_embedding_model

def create_vector_store(chunks):
    embedding_model = get_embedding_model()

    vector_db = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    vector_db.save_local("faiss_index")

    print("FAISS vector database created successfully!")

    return vector_db