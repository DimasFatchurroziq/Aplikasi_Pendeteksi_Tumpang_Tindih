import os

from extract_utils import Extractor
from split_utils import Splitter
from sbert_utils import SentenceBert
from cosinesimilarity_utils import CosineSimilarity

# Step 1: Akses ke file / ddb
pdf_path_1 = "../file/file_1"
pdf_path_2 = "../file/file_2"
files_1 = os.listdir(pdf_path_1)
files_2 = os.listdir(pdf_path_2)

files_1 = [f for f in files_1 if os.path.isfile(os.path.join(pdf_path_1, f))]
files_2 = [f for f in files_2 if os.path.isfile(os.path.join(pdf_path_2, f))]

extractor = Extractor(files_1)
text = extractor.extract_pdf_to_text()


splitter = Splitter(text)
generator_aturan = splitter.split_text_to_rule()

sberter = SentenceBert(generator_aturan)
embedding = sberter.get_embedding_palsu()

num = len(generator_aturan)
cosine = CosineSimilarity(embedding, num)
hasil_cosine = cosine.calculate_similarity()


# for list_tuple in generator_aturan:
#     pasal_hehe = list_tuple[0]
#     ayat_hehe = list_tuple[1]
#     print(pasal_hehe, ayat_hehe)
#         # print(hasil_cosine) 
print(hasil_cosine)

jumlah_akhir = len(hasil_cosine)

jumlah_harusnya = num*(num-1)/2

if jumlah_akhir == jumlah_harusnya:
    print("Benar sekali")
else:
    print("wkwk")



# Step 3: Simpan ke database langsung
# buat_tabel()
# simpan_ke_db_bulk(generator_aturan)





