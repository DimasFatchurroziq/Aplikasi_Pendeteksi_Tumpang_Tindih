from django.db import models

class File(models.Model):
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Rule(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='rules')
    rule_text = models.TextField()
    rule_number = models.CharField(max_length=100)  # contoh: Pasal 5 Ayat (2)

    def __str__(self):
        return f"{self.rule_number} - {self.file.name}"

class Comparison(models.Model):
    INTRA = 'intra'
    INTER = 'inter'
    SCOPE_CHOICES = [
        (INTRA, 'Intra-file'),
        (INTER, 'Inter-file'),
    ]

    rule_a = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='comparison_as_a')
    rule_b = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='comparison_as_b')
    similarity = models.FloatField()
    verdict = models.CharField(max_length=20)  # entailment, contradiction, neutral
    scope = models.CharField(max_length=10, choices=SCOPE_CHOICES)

    def __str__(self):
        return f"{self.rule_a} <-> {self.rule_b} [{self.verdict}]"
