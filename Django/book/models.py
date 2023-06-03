from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    url = models.CharField(max_length=1000, null=True, blank=True)
