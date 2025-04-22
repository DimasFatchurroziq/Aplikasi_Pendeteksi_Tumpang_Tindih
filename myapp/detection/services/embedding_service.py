from utils.sbert_utils import SentenceBert

class EmbeddingService:
    def __init__(self, embedding_service):
        self.rule_repository = rule_repository
    
    def sbert_embedded(self, file):
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
