from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from .vector_database import create_vector_database


def process_all_pdfs(folder_path="data"):

    folder = Path(folder_path)

    all_documents = []

    # Load every PDF in the data folder
    for pdf_file in folder.glob("*.pdf"):

        print(f"Loading: {pdf_file.name}")

        loader = PyMuPDFLoader(
            str(pdf_file)
        )

        documents = loader.load()

        # Store PDF filename in metadata
        for document in documents:

            document.metadata["source_file"] = (
                pdf_file.name
            )

        all_documents.extend(documents)


    # Split documents into chunks

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(
        all_documents
    )


    # Create combined FAISS database

    create_vector_database(
        chunks
    )


    return (
        len(all_documents),
        len(chunks)
    )