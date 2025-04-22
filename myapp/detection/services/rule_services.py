from utils.extract_utils import Extractor
from utils.splitter_utils import Splitter

class RuleService:
    def __init__(self, rule_repository):
        self.rule_repository = rule_repository

    def extract_and_split(self, file):
        extractor = Extractor(file)
        text = extractor.extract_pdf_to_text()

        splitter = Splitter(text)
        rules = splitter.split_text_to_rule()

        saved_rules = []
        for rule in rules:
            saved = self.rule_repository.save_rule({
                "file": self.file,
                "content": rule
            })
            saved_rules.append(saved)

        return saved_rules

