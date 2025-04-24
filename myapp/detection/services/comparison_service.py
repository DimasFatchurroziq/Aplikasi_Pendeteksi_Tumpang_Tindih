import pickle
from detection.models import Comparison

class EmbeddingService:
    def __init__(self, comparison_repository):
        self.comparison_repository = comparison_repository
    
    def comparing_rule(self, list_rule_objects):
        sentencebert = SentenceBert()
        list_embeddings = sentencebert.embedding_content_tupple(list_rule_objects)

        for rule, embedding in zip(list_rule_objects, list_embeddings):
            self.embedding_repository.save_embedding({
                "rule": rule,
                "embedding": pickle.dumps(embedding) 
            })

        return list_embeddings