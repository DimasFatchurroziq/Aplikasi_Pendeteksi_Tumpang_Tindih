import os
import django
import sys

# Set path ke root Django project (folder yang ada manage.py)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")  # ganti 'myapp' dengan nama projectmu

django.setup()

from django.core.files.uploadedfile import SimpleUploadedFile
from detection.factories.factory import get_file_service
from detection.factories.factory import get_rule_service
from detection.factories.factory import get_embedding_service
from detection.factories.factory import get_comparison_service

def upload_file_to_db(path_file_list):

    if len(path_file_list) != 2:
        print("❌ Harus tepat 2 file untuk dibandingkan.")
        return

    file_service_1 = get_file_service()
    file_service_2 = get_file_service()

    # === File pertama ===
    with open(path_file_list[0], "rb") as f1:
        uploaded_1 = SimpleUploadedFile(
            name=os.path.basename(path_file_list[0]),
            content=f1.read(),
            content_type='application/pdf'
        )
    file_instance_1 = file_service_1.handle_save_file(uploaded_1)

    # === File kedua ===
    with open(path_file_list[1], "rb") as f2:
        uploaded_2 = SimpleUploadedFile(
            name=os.path.basename(path_file_list[1]),
            content=f2.read(),
            content_type='application/pdf'
        )
    file_instance_2 = file_service_2.handle_save_file(uploaded_2)

    print(f"[✓] File berhasil disimpan ke DB: {file_instance_1.name}, {file_instance_2.name}")
    # print("Path file di DB:", file_instance.file.path)


    rule_service_1 = get_rule_service()
    rule_service_2 = get_rule_service()

    list_rule_objects_1 = rule_service_1.extract_and_split(file_instance_1)
    list_rule_objects_2 = rule_service_2.extract_and_split(file_instance_2)
    print(f"[✓] {len(list_rule_objects_1)}, {len(list_rule_objects_2)} aturan berhasil diekstrak")

    
    embedding_service_1 = get_embedding_service()
    embedding_service_2 = get_embedding_service()

    list_embeddings_1 = embedding_service_1.sbert_embedded(list_rule_objects_1)
    list_embeddings_2 = embedding_service_2.sbert_embedded(list_rule_objects_2)
    print(f"[✓] Embedding selesai untuk {len(list_embeddings_1)}, {len(list_embeddings_2)} aturan")


    comparison_service = get_comparison_service()

    list_compare = comparison_service.comparing_rule_diff_doc(list_rule_objects_1, list_rule_objects_2, list_embeddings_1, list_embeddings_2)
    print(f"[✓] Comparing selesai untuk {len(list_compare)} aturan")

if __name__ == "__main__":
    # Path ke file PDF yang ingin di-upload
    file_paths = [
        os.path.join("file", "file_2", "akademik_1.pdf"),
        os.path.join("file", "file_2", "akademik_2.pdf")
    ]
    upload_file_to_db(file_paths)
    
