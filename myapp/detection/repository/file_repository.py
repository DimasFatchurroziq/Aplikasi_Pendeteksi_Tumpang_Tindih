from detection.models import File

class FileRepository:
    @staticmethod
    def get_all_files():
        return File.objects.all()

    @staticmethod
    def save_file(name, file):
        return File.objects.create(name=name, file=file)

    @staticmethod
    def delete_file(file_id):
        file = File.objects.get(id=file_id)
        file.delete()
        return file
