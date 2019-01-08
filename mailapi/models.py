from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Mails(models.Model):
    von = models.EmailField()
    objekt = models.CharField(max_length=120, blank=True)
    text = models.TextField(max_length=2000000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.objekt
