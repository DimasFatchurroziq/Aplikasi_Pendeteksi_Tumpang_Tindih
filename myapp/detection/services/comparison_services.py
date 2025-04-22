from detection.models import Comparison

# CREATE
def create_comparison(rule_a, rule_b, similarity, verdict, scope):
    return Comparison.objects.create(
        rule_a=rule_a,
        rule_b=rule_b,
        similarity=similarity,
        verdict=verdict,
        scope=scope
    )

# READ
def get_comparisons_by_scope(scope):
    return Comparison.objects.filter(scope=scope)

# UPDATE
def update_comparison(comp_id, similarity=None, verdict=None):
    comp = Comparison.objects.get(id=comp_id)
    if similarity is not None:
        comp.similarity = similarity
    if verdict:
        comp.verdict = verdict
    comp.save()
    return comp

# DELETE
def delete_comparison(comp_id):
    Comparison.objects.get(id=comp_id).delete()
