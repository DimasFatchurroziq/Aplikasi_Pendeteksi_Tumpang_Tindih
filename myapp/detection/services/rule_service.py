from utils.extract_util import Extractor
from utils.split_util import Splitter

class RuleService:
    def __init__(self, rule_repository):
        self.rule_repository = rule_repository

    def extract_and_split(self, file):
        # Pastikan kita passing path ke file PDF, bukan objek atau nama file
        extractor = Extractor(file.file.path)
        text = extractor.extract_pdf_to_text()

        splitter = Splitter(text)
        rules = splitter.split_text_to_rule()

        list_contents = []
        for rule in rules:
            saved = self.rule_repository.save_rule({
                "file": file,  # gunakan parameter `file` langsung (bukan self.file)
                "article_num": rule[0],
                "section_num": rule[1],
                "point_num": rule[2],
                "content": rule[3]
            })

            list_contents.append(saved) 

        return list_contents
