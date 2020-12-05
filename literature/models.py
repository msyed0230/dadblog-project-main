from django.db import models

class Literature(models.Model):
    body = models.TextField(max_length=500, default='')
    image = models.ImageField(upload_to='images/')
