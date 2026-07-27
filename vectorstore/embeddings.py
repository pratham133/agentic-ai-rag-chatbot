from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config.settings import settings


class EmbeddingService:

    def __init__(self):

        self.embeddings = GoogleGenerativeAIEmbeddings(
            model=settings.embedding_model,
            google_api_key=settings.google_api_key,
        )

    def embed_documents(self, texts):
        return self.embeddings.embed_documents(texts)

    def embed_query(self, query):
        return self.embeddings.embed_query(query)