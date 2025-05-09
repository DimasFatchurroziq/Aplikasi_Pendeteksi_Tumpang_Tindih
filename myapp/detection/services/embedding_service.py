import pickle
from utils.sbert_util  import SentenceBert

class EmbeddingService:
    def __init__(self, embedding_repository):
        self.embedding_repository = embedding_repository
    
    def sbert_embedded(self, list_rule_objects):
        sentencebert = SentenceBert()
        list_embeddings = sentencebert.embedding_content_tupple(list_rule_objects)

        for rule, embedding in zip(list_rule_objects, list_embeddings):
            self.embedding_repository.save_embedding({
                "rule": rule,
                "embedding": pickle.dumps(embedding) 
            })

        return list_embeddings
