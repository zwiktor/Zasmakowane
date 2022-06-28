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
    cuisines = models.ManyToManyField(Cuisine)
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)

class Ingredient(models.Model):
    measurment = [
        ('GR', 'Gramy'),
        ('ML', 'Mililitry'),
    ]
    name = models.CharField(max_length=128, default='Produkt')
    measure = models.CharField(max_length=2, choices=measurment, default='GR')
    quantity = models.IntegerField(default=1)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return ' '.join([self.name, str(self.quantity), self.measure])


class Step(models.Model):
    number = models.IntegerField(default=1)
    description = models.CharField(max_length=1024, default='Opis kroku')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number) + ' Krok'

    def save(self, *args, **kwargs):
        steps = Step.objects.filter(recipe=self.recipe)
        steps_count = len(steps)
        if self.number > steps_count or self.number == None:
            self.number = steps_count + 1
        else:
            steps_to_up = steps[self.number-1:]
            for step_to_up in steps_to_up:
                step_to_up.number += 1
                step_to_up.save()
        super(Step, self).save(*args, **kwargs)
