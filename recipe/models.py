from django.db import models


class Cuisine(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=256, default='Przepis')
    description = models.TextField(default='krotki opis')

