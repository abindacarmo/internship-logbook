from django.db import models

# Create your models here.

class Aktivitas(models.Model):
    date_ohin = models.DateField()
    oras_hahu = models.TimeField(null=True, blank=True)
    oras_hotu = models.TimeField(null=True, blank=True)
    atividade = models.CharField(max_length=255)
    deskrisaun = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_ohin', 'oras_hahu']
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f"{self.date_ohin} - {self.atividade}"