import pickle
from utils.cosinesimilarity_util import CosineSimilarity

class ComparisonService:
    def __init__(self, comparison_repository):
        self.comparison_repository = comparison_repository
        
    def comparing_rule_same_doc(self, list_rule_objects, list_embeddings):
        hasil = []
        many_articles = len(list_embeddings)
        for i in range(many_articles):
            for j in range(i + 1, many_articles):
                cosinesimilarity = CosineSimilarity()
                compare = cosinesimilarity.calculate_similarity(list_embeddings[i], list_embeddings[j])
                saved = self.comparison_repository.save_comparison({
                    "rule_1": list_rule_objects[i],
                    "rule_2": list_rule_objects[j],
                    "similarity_score": compare,
                    "scenario": "same_doc",
                })
                hasil.append(saved)
        return hasil

    def comparing_rule_diff_doc(self, list_rule_objects_1, list_rule_objects_2, list_embeddings_1, list_embeddings_2):
        hasil = []
        many_articles_1 = len(list_embeddings_1)
        many_articles_2 = len(list_embeddings_2)
        for i in range(many_articles_1):
            for j in range(many_articles_2):
                cosinesimilarity = CosineSimilarity()
                compare = cosinesimilarity.calculate_similarity(list_embeddings_1[i], list_embeddings_2[j])
                saved = self.comparison_repository.save_comparison({
                    "rule_1": list_rule_objects_1[i],
                    "rule_2": list_rule_objects_2[j],
                    "similarity_score": compare,
                    "scenario": "diff_doc",
                })
                hasil.append(saved)
        return hasil