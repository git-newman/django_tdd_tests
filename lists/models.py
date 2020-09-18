from django.db import models

# Create your models here.


class Item(models.Model):
    text = models.TextField(default='')

    def __str__(self):
        """строковое представление модели"""
        return self.text
