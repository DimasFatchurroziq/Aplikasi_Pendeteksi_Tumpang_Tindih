import re

class Splitter:
    def __init__(self, text):
        self.text = text.replace('\n', ' ')  # hapus newline

    def article_splitter(self):
        article_pattern = article_pattern = r"Pasal\s(\d+)\s+(.*?)(?=Pasal\s\d+|\bBab|\Z)"
        return re.findall(article_pattern, self.text, re.IGNORECASE | re.DOTALL)

    def section_splitter(self, article_content):
        section_pattern = r"\((\d+)\)\s*(.*?)(?=\(\d+\)|$)"
        return re.findall(section_pattern, article_content, re.DOTALL)

    def split_text_to_rule(self):
        sections_result = []
        for article_num, article_content in self.article_splitter():
            sections = self.section_splitter(article_content)
            if sections:
                for section_num, section_content in sections:
                    sections_result.append((article_num, section_num, section_content.strip()))
            else:
                sections_result.append((article_num, 0, article_content.strip()))

        return sections_result
