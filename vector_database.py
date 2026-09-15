from langchain_community.vectorstores import FAISS
from .embeddings import get_embeddings


def create_vector_database(chunks, save_path="vectorstore"):

    embeddings = get_embeddings()

    vector_database = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_database.save_local(save_path)

    return vector_database