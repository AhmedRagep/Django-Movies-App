from django.utils import timezone
from typing import Iterable, Optional
from django.db import models
from django.utils.text import slugify
# Create your models here.

CATEGORY_CHOICES = {
    ('action','ACTION'),
    ('drama','DRAMA'),
    ('comedy','COMEDY'),
    ('romance','ROMANCE'),
}

LANGUAGE_CHOICES = {
    ('english','ENGLISH'),
    ('german','GERMAN'),
}

STATUS_CHOICES = {
    ('RA','RESENTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED'),
}

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movie_image')
    banner = models.ImageField(upload_to='movie_banner', blank=False, null=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    cast = models.CharField(max_length=200)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    trailer = models.URLField()
    slug = models.SlugField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Movie, self).save(*args, **kwargs)


    class Meta:
        verbose_name = ("Movie")
        verbose_name_plural = ("Movies")

    def __str__(self):
        return self.title
    

LINK_CHOICES = (
    ('D','DOWNLOAD_LINKS'),
    ('W','WATCH_LINKS'),
)
class Movie_Links(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_links', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    links = models.URLField()
    
    def __str__(self):
        return str(self.movie)
