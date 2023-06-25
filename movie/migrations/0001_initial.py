# Generated by Django 4.2.2 on 2023-06-11 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='movie')),
                ('category', models.CharField(choices=[('A', 'ACTION'), ('D', 'DRAMA'), ('C', 'COMEDY'), ('R', 'ROMANCE')], max_length=1)),
                ('language', models.CharField(choices=[('EN', 'ENGLISH'), ('GR', 'GERMAN')], max_length=2)),
                ('status', models.CharField(choices=[('RA', 'RESENTLY ADDED'), ('MW', 'MOST WATCHED'), ('TR', 'TOP RATED')], max_length=2)),
                ('year_of_production', models.DateField()),
                ('views_count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]