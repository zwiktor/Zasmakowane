from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=256, default='Przepis')
    description = models.TextField(default='krotki opis')

