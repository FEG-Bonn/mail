# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1200)
    background_image = models.FileField(null= True, blank= True, upload_to="user/data/uploads")
    time = models.fields.DateTimeField(blank = True, null = True, auto_now=True, auto_created=True)

    def __str__(self):
        return str(self.title)+", Last editing: "+str(self.time)
