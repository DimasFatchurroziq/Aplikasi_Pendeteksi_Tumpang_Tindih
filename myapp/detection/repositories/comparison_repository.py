from detection.models import Comparison

class ComparisonRepository:
    @staticmethod
    def get_all_comparisons():
        return Comparison.objects.all()

    @staticmethod
    def save_comparison(data):
        return Comparison.objects.create(
            rule_1=data["rule_1"],
            rule_2=data["rule_2"],
            similarity_score=data["similarity_score"],
            scenario=data["scenario"],
        )
    
    # @staticmethod
    # def get_comparison_by_rule(rule_id):
    #     return Comparison.objects.filter(rule_id=rule_id)