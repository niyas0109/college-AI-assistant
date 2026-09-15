import streamlit as st
from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.rag_pipeline import ask_question
from src.vector_database import create_vector_database


st.set_page_config(
    page_title="AI College Assistant",
    page_icon="🎓",
    layout="wide"
)


# Initialize chat memory BEFORE sidebar
if "messages" not in st.session_state:
    st.session_state.messages = []


def process_all_pdfs(folder_path="data"):

    folder = Path(folder_path)

    all_documents = []

    pdf_files = list(folder.glob("*.pdf"))

    if not pdf_files:
        return 0, 0

    for pdf_file in pdf_files:

        loader = PyMuPDFLoader(
            str(pdf_file)
        )

        documents = loader.load()

        for document in documents:

            document.metadata["source_file"] = (
                pdf_file.name
            )

        all_documents.extend(documents)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(
        all_documents
    )

    create_vector_database(chunks)

    return len(all_documents), len(chunks)


# Title
st.title("🎓 AI College Assistant")

st.write(
    "Ask questions about your college and university "
    "documents using Gemini + RAG."
)


# Sidebar
with st.sidebar:

    st.header("📚 Documents")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        if st.button("📥 Add PDF"):

            data_folder = Path("data")

            data_folder.mkdir(
                exist_ok=True
            )

            pdf_path = (
                data_folder /
                uploaded_file.name
            )

            with open(
                pdf_path,
                "wb"
            ) as file:

                file.write(
                    uploaded_file.getbuffer()
                )

            st.success(
                f"Added: {uploaded_file.name}"
            )

    st.divider()

    st.subheader("📄 Available PDFs")

    data_folder = Path("data")

    if data_folder.exists():

        pdf_files = list(
            data_folder.glob("*.pdf")
        )

        for pdf_file in pdf_files:

            st.write(
                f"📄 {pdf_file.name}"
            )

    st.divider()

    if st.button("🔄 Build Knowledge Base"):

        with st.spinner(
            "Processing PDFs..."
        ):

            try:

                documents, chunks = (
                    process_all_pdfs("data")
                )

                st.success(
                    "Knowledge base created!"
                )

                st.write(
                    f"📄 Pages: {documents}"
                )

                st.write(
                    f"🧩 Chunks: {chunks}"
                )

                st.cache_resource.clear()

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )

    st.divider()

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

        if "sources" in message:

            with st.expander(
                "📚 Sources"
            ):

                for source in message["sources"]:

                    st.write(
                        f"📄 {source['filename']} "
                        f"- Page {source['page']}"
                    )

                    st.caption(
                        source["excerpt"]
                    )


# Welcome message
if not st.session_state.messages:

    st.info(
        """
        👋 Welcome to AI College Assistant!

        Try asking:

        • What is the minimum attendance requirement?

        • What happens if attendance is below 75%?

        • What are the examination regulations?
        """
    )


# Chat input
question = st.chat_input(
    "Ask something about your documents..."
)


if question:

    # Save user question
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(
            question
        )


    # Generate AI answer
    with st.chat_message("assistant"):

        with st.spinner(
            "🔎 Searching documents..."
        ):

            try:

                # Do not include current question
                # twice in conversation history
                chat_history = (
                    st.session_state.messages[:-1]
                )

                answer, results = ask_question(
                    question,
                    chat_history
                )

                st.markdown(
                    answer
                )


                # Collect sources
                sources = []

                for result in results:

                    page = result.metadata.get(
                        "page"
                    )

                    filename = result.metadata.get(
                        "source_file",
                        "Unknown PDF"
                    )

                    if page is not None:

                        sources.append(
                            {
                                "filename": filename,
                                "page": page + 1,
                                "excerpt": result.page_content
                            }
                        )


                # Remove duplicate sources
                unique_sources = []

                seen = set()

                for source in sources:

                    key = (
                        source["filename"],
                        source["page"]
                    )

                    if key not in seen:

                        seen.add(key)

                        unique_sources.append(
                            source
                        )


                # Display sources
                if unique_sources:

                    with st.expander(
                        "📚 Sources & Relevant Text"
                    ):

                        for source in unique_sources:

                            st.write(
                                f"📄 {source['filename']} "
                                f"- Page {source['page']}"
                            )

                            st.caption(
                                source["excerpt"]
                            )


                # Save assistant message
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": unique_sources
                    }
                )


            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )

