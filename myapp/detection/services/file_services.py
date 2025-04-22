from repository.file_repository import FileRepository

class FileService:
    def __init__(self, file_repository):
        self.file_repository = file_repository

    def handle_save_file(self, uploaded_file):
        return self.file_repository.save_file({
            "name": uploaded_file.name,
            "file": uploaded_file
        })

    def handle_deleted_file(self, file_id):
        return self.file_repository.delete_file(file_id)

    def handle_get_file(self):
        return self.file_repository.get_all_files()

    
