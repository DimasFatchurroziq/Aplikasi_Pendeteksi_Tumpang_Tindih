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
    list_contents = rule_service.extract_and_split(file_instance)
    print(f"[✓] {len(list_contents)} aturan berhasil diekstrak")

    # print(list_contents)

    
    embedding_service = get_embedding_service()
    embedded = embedding_service.sbert_embedded(list_contents)
    print(f"[✓] Embedding selesai untuk {len(embedded)} aturan")


# def run(file_instance):
#     rule_service = get_rule_service()
#     list_tuple_rules = rule_service.extract_and_split(file_instance)
#     print(f"[✓] {len(list_tuple_rules)} aturan berhasil diekstrak")

if __name__ == "__main__":
    # Path ke file PDF yang ingin di-upload
    path_file = os.path.join("file", "file_1", "ujicoba.pdf")
    upload_file_to_db(path_file)


# list_tuple_rules = RuleService.extract_and_split(file_instance)
# embedded = EmbeddingService.sbert_embedded(list_tuple_rules)
# comparisons = ComparisonService.compare_within_rules(embedded)