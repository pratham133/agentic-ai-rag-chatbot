"""
Document Ingestion Module

Loads the PDF knowledge base and splits it into
overlapping chunks ready for embedding.
"""

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


class DocumentIngestor:
    """
    Loads and chunks the PDF knowledge base.
    """

    def __init__(
        self,
        pdf_path: str,
        chunk_size: int = 800,
        chunk_overlap: int = 150,
    ):
        self.pdf_path = pdf_path

        self.loader = PyMuPDFLoader(pdf_path)

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def load_documents(self) -> list[Document]:
        """
        Load PDF into LangChain Document objects.
        """
        return self.loader.load()

    def split_documents(
        self,
        documents: list[Document]
    ) -> list[Document]:
        """
        Split documents into smaller chunks.
        """
        return self.text_splitter.split_documents(documents)

    def ingest(self) -> list[Document]:
        """
        Complete ingestion pipeline.
        """
        documents = self.load_documents()

        chunks = self.split_documents(documents)

        return chunks