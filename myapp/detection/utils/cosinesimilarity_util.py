from sentence_transformers import util
import torch

class CosineSimilarity:
    def calculate_similarity(self, embedding_1, embedding_2):
        similarity_score = util.cos_sim(embedding_1, embedding_2)
        return similarity_score
    


