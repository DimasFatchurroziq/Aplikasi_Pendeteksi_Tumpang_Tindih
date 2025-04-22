from sentence_transformers import SentenceTransformer

class SentenceBert:
    def __init__(self, model_name="firqaaa/indo-sentence-bert-base"):
        # self.list_pasal_palsu = []
        # for tuple_palsu in pasals:
        #     pasal_palsu = tuple_palsu[2]
        #     self.list_pasal_palsu.append(pasal_palsu)
        # self.pasals = pasals #yg asli, nnti hrus di uncomment
        self.model = SentenceTransformer(model_name)

    def update_embedding_to_tuple(self, list_tuple_rules):
        self.list_content = []
        for tuple in self.list_tuple_rules:
            content = tuple[2]
            self.list_content.append(content)
        list_embedding = self.get_embedding(list_content)
        for 

    def get_embedding(self, list_content):
        """Mengubah kalimat menjadi embedding vektor"""
        embeddings = self.model.encode(self.list_content, convert_to_tensor=True)
        return embeddings

    # def get_embedding_palsu(self):
    #     """Mengubah kalimat menjadi embedding vektor"""
    #     embeddings = self.model.encode(self.list_pasal_palsu, convert_to_tensor=True)
    #     return embeddings















# if __name__ == "__main__":
#     pasals = [
#         "Pasal 1 Setiap warga negara berhak atas pendidikan.",
#         "Pasal 2 Pendidikan adalah hak semua orang.",
#         "Pasal 3 Negara menjamin pendidikan yang layak.",
#         "Pasal 4 Setiap orang berhak atas tempat tinggal."
#     ]
#     comparer = SentenceBert(pasals)

#     skor = comparer.get_embedding()

#     cosine = CosineSimialirity(skor, pasals).calculate_similarity()
#     print(cosine)
#     # print(f"Kemiripan: {skor:.4f}")


