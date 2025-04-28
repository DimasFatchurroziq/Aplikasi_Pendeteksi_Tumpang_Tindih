from sentence_transformers import util
import torch

class CosineSimilarity:
    # def __init__(self, comparison_repository): #nnti di akhir tambahi embedding2,
    #     self.comparison_repository = comparison_repository

    # def calculate_similarity(self, embedding_1):
    #     hasil = []
    #     many_articles = len(embedding_1)
    #     for i in range(many_articles):
    #         for j in range(i + 1, many_articles):
    #             similarity_score = util.cos_sim(embedding_1[i], embedding_1[j])
    #             formatted_score = round(similarity_score.item(), 4)  # dibulatkan 4 angka di belakang koma
    #             hasil.append(formatted_score)
    #     return hasil

    def calculate_similarity(self, embedding_1, embedding_2):
        similarity_score = util.cos_sim(embedding_1, embedding_2)
        return similarity_score
    


