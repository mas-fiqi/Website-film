from django.db import models

# Create your models here.
class Film(models.Model):
    Userid = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.Userid}, {self.password}"