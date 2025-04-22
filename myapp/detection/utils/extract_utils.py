import fitz 

class Extractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_pdf_to_text(self):
        doc = fitz.open(self.pdf_path[0])
        extracted_text = ""
        for page in doc:
            extracted_text += page.get_text()

        doc.close()
        return extracted_text

