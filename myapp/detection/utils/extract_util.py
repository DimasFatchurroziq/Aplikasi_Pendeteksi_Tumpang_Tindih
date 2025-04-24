import fitz 
import mimetypes

class Extractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_pdf_to_text(self):
        mime_type, _ = mimetypes.guess_type(self.pdf_path)
        if mime_type != "application/pdf":
            raise ValueError("File bukan PDF yang valid.")

        doc = fitz.open(self.pdf_path)
        extracted_text = ""
        for page in doc:
            extracted_text += page.get_text()

        doc.close()
        return extracted_text

