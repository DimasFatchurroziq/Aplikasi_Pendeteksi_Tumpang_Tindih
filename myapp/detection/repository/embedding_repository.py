from detection.models import Embedding

class EmbeddingRepository:
    def get_all_embeddings(self):
        return Embedding.objects.all()

    def save_embedding(self, embedding_data):
        return Embedding.objects.create(**embedding_data)