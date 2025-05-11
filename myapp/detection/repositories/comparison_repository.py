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
    
