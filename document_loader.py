from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(folder_path):
    documents = []

    folder = Path(folder_path)

    for pdf_file in folder.glob("*.pdf"):
        print(f"Loading: {pdf_file.name}")

        loader = PyMuPDFLoader(str(pdf_file))
        pdf_documents = loader.load()

        documents.extend(pdf_documents)

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    return chunks