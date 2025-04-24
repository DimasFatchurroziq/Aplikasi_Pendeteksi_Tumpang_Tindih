from detection.models import RuleEmbedding

class EmbeddingRepository:
    @staticmethod
    def get_all_embeddings():
        return RuleEmbedding.objects.all()

    @staticmethod
    def save_embedding(data):
        return RuleEmbedding.objects.create(
            rule=data["rule"],
            embedding=data["embedding"]
        )
    
    @staticmethod
    def get_embedding_by_rule(rule_id):
        return RuleEmbedding.objects.filter(rule_id=rule_id)