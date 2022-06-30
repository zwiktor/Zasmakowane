# Generated by Django 3.2.13 on 2022-06-30 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0014_alter_recipe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
        ),
    ]