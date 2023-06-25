# Generated by Django 4.2.2 on 2023-06-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_movie_category_alter_movie_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('comedy', 'COMEDY'), ('drama', 'DRAMA'), ('action', 'ACTION'), ('romance', 'ROMANCE')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('german', 'GERMAN'), ('english', 'ENGLISH')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('MW', 'MOST WATCHED'), ('TR', 'TOP RATED'), ('RA', 'RESENTLY ADDED')], max_length=2),
        ),
    ]
