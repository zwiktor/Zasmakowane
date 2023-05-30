from django.db import models
from django.utils.text import slugify
from django.utils import timezone

from Blog.settings import MEDIA_URL

class Cuisine(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=2, default='T')
    color = models.CharField(max_length=7, default='#ff5733')


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=256, default='Przepis')
    short_description = models.TextField(default='krotki opis')
    description = models.TextField(default='dlugi opis opis')
    prep_time = models.SmallIntegerField(null=True)
    cooking_time = models.SmallIntegerField(null=True)
    sum_time = models.SmallIntegerField(null=True)
    calories = models.DecimalField(decimal_places=1, max_digits=6, null=True)
    portions = models.SmallIntegerField(null=True)
    calories_per_portion = models.DecimalField(decimal_places=1, max_digits=5, null=True)
    carb = models.DecimalField(decimal_places=1, max_digits=5,null=True)
    protein = models.DecimalField(decimal_places=1, max_digits=5,null=True)
    fat = models.DecimalField(decimal_places=1, max_digits=5,null=True)
    cuisines = models.ManyToManyField(Cuisine)
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)
    small_photo = models.ImageField()
    big_photo_1 = models.ImageField()
    big_photo_2 = models.ImageField(null=True)
    create_date = models.DateTimeField(null=True)
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
        if not self.id:
            self.create_date = timezone.now()

        super(Recipe, self).save(*args, **kwargs)


class Ingedient_group(models.Model):
    name = models.CharField(max_length=128, default='Produkt')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe.title + ' - ' + self.name


class Ingredient(models.Model):
    measurment = [
        ('gr', 'Gramy'),
        ('ml', 'Mililitry'),
    ]
    name = models.CharField(max_length=128, default='Produkt')
    measure = models.CharField(max_length=2, choices=measurment, default='', blank=True, null=True)
    quantity = models.IntegerField(default=None, null=True, blank=True)
    group = models.ForeignKey(Ingedient_group, on_delete=models.CASCADE)

    def __str__(self):
        if self.quantity and self.measure:
            return self.group.recipe.title + ' - ' + self.group.name + ' - ' + self.name
        return self.name

class Step(models.Model):
    number = models.IntegerField(default=0)
    description = models.TextField(default='Opis kroku')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe.title + ' - ' +  str(self.number) + ' Krok'

    # def save(self, *args, **kwargs):
    #     steps = Step.objects.filter(recipe=self.recipe)
    #     self.number = len(steps) + 1
    #     super(Step, self).save(*args, **kwargs)

class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)