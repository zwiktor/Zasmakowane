# Generated by Django 3.2.13 on 2022-06-28 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_recipe_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe'),
            preserve_default=False,
        ),
    ]
