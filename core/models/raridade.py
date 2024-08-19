from django.db import models

class Raridade(models.Model):
    tier = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tier} - ({self.id})"