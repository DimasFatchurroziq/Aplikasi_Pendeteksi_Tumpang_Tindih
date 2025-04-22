from django.db import models

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdf_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Rule(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='rules')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rule from {self.file.name[:30]}"

class RuleEmbedding(models.Model):
    rule = models.OneToOneField(Rule, on_delete=models.CASCADE, related_name='embedding')
    embedding = models.BinaryField()  # Atau JSONField jika pakai array/list

class Comparison(models.Model):
    rule1 = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='comparisons_from')
    rule2 = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='comparisons_to')
    similarity_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comparison ({self.similarity_score:.2f})"
