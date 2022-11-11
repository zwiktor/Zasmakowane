from django.db import models
from django.utils.text import slugify

from Blog.settings import MEDIA_URL

class Cuisine(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=256, default='Przepis')
    description = models.TextField(default='krotki opis')
    prep_time = models.SmallIntegerField()
    calories = models.SmallIntegerField(null=True)
    carb = models.SmallIntegerField(null=True)
    protein = models.SmallIntegerField(null=True)
    fat = models.SmallIntegerField(null=True)
    cuisines = models.ManyToManyField(Cuisine)
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)
    small_photo = models.ImageField()
    big_photo_1 = models.ImageField()
    big_photo_2 = models.ImageField(null=True)
    create_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    def save(self,*args, **kwargs):
        numer_of_same_slug = len(Recipe.objects.filter(title=self.title))
        if numer_of_same_slug > 0:
            s = f'{self.title}-{numer_of_same_slug}'
        else:
            s = self.title
        if not self.slug:
            self.slug = slugify(s)
        super(Recipe, self).save(*args, **kwargs)

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
    number = models.IntegerField(default=0)
    description = models.TextField(default='Opis kroku')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe.title + ' - ' +  str(self.number) + ' Krok'

    def save(self, *args, **kwargs):
        steps = Step.objects.filter(recipe=self.recipe)
        self.number = len(steps) + 1
        super(Step, self).save(*args, **kwargs)

class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)