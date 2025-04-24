from detection.models import Rule

class RuleRepository:
    @staticmethod
    def get_all_rules():
        return Rule.objects.all()

    @staticmethod
    def save_rule(data):
        return Rule.objects.create(
            file=data["file"],
            article_num=data["article_num"],
            section_num=data["section_num"],
            content=data["content"]
        )

    @staticmethod
    def get_rules_by_file(file_id):
        return Rule.objects.filter(file_id=file_id)

