from django.db import models

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdf_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Rule(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='rules')
    article_num = models.TextField()
    section_num = models.TextField(null=True, blank=True)
    point_num = models.TextField(null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rule from {self.file.name[:30]}"

class RuleEmbedding(models.Model):
    rule = models.OneToOneField(Rule, on_delete=models.CASCADE, related_name='embedding')
    embedding = models.BinaryField()  # Atau JSONField jika pakai array/list
    created_at = models.DateTimeField(auto_now_add=True)
    
class Comparison(models.Model):
    rule_1 = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='comparisons_from')
    rule_2 = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='comparisons_to')
    similarity_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    SCENARIO_CHOICES = [
        ('same_doc', 'Same Document'),
        ('diff_doc', 'Different Document'),
    ]

    scenario = models.CharField(max_length=20, choices=SCENARIO_CHOICES, default='same_doc')

    def __str__(self):
        score = self.similarity_score
        if isinstance(score, torch.Tensor):
            score = score.item()
        return f"Comparison ({score:.2f}) - {self.get_scenario_display()}"

