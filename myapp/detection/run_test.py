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

def upload_file_to_db(path_file):
    file_service = get_file_service()

    with open(path_file, "rb") as f:
        uploaded = SimpleUploadedFile(
            name=os.path.basename(path_file),
            content=f.read(),
            content_type='application/pdf'
        )

    file_instance = file_service.handle_save_file(uploaded)
    print(f"[✓] File berhasil disimpan ke DB: {file_instance.name}")
    print("Path file di DB:", file_instance.file.path)


    rule_service = get_rule_service()
    list_rule_objects = rule_service.extract_and_split(file_instance)
    print(f"[✓] {len(list_rule_objects)} aturan berhasil diekstrak")


    
    embedding_service = get_embedding_service()
    list_embeddings = embedding_service.sbert_embedded(list_rule_objects)
    print(f"[✓] Embedding selesai untuk {len(list_embeddings)} aturan")


    comparison_service = get_comparison_service()
    list_compare = comparison_service.comparing_rule_same_doc(list_rule_objects, list_embeddings)
    print(f"[✓] Comparing selesai untuk {len(list_compare)} aturan")

if __name__ == "__main__":
    # Path ke file PDF yang ingin di-upload
    path_file = os.path.join("file", "file_1", "asu1.pdf")
    upload_file_to_db(path_file)
