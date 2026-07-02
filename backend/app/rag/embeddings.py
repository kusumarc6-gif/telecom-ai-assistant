from langchain_huggingface import HuggingFaceEmbeddings

# Load HuggingFace embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def get_embedding_model():
    return embedding_model