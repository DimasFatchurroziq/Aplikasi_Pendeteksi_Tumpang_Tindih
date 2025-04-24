from detection.models import Comparison

class ComparisonRepository:
    @staticmethod
    def get_all_comparisons():
        return Comparison.objects.all()

    @staticmethod
    def save_comparison(data):
        return Comparison.objects.create(
            rule=data["rule"],
            comparison=data["comparison"]
        )
    
    @staticmethod
    def get_comparison_by_rule(rule_id):
        return Comparison.objects.filter(rule_id=rule_id)