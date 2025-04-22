from sentence_transformers import util
import torch

class CosineSimilarity:
    def __init__(self, embedding1, pasals): #nnti di akhir tambahi embedding2,
        self.embedding1 = embedding1
        # self.embedding2 = embedding2
        self.num_pasals = pasals

    def calculate_similarity(self):
        hasil = []
        num_pasals = len(self.embedding1)
        for i in range(num_pasals):
            for j in range(i + 1, num_pasals):
                similarity_score = util.cos_sim(self.embedding1[i], self.embedding1[j])
                formatted_score = round(similarity_score.item(), 4)  # dibulatkan 4 angka di belakang koma
                hasil.append(formatted_score)
        return hasil
    


