from detection.models import Rule

class RuleRepository:
    @staticmethod
    def get_all_rules():
        return File.objects.all()

    @staticmethod
    def save_rule(rule_data):
        return Rule.objects.create(**rule_data)

    @staticmethod
    def get_rules_by_file(file_id):
        return Rule.objects.filter(file_id=file_id)

