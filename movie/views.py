from typing import Any, Dict, Optional
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie ,Movie_Links
# Create your views here.

class MovieListView(ListView):
    model = Movie
    paginate_by = 2
    template_name = 'movie/list.html'


# -----------------
class Home(ListView):
    model = Movie
    template_name = 'movie/home.html'

    def get_context_data(self, **kwargs):
        # هات كل الافلام اللي فيها الجاتيجوري دي 
        context = super(Home, self).get_context_data(**kwargs)
        # ورجعها في المتغير ده
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_watched'] = Movie.objects.filter(status='MW')
        context['resent_added'] = Movie.objects.filter(status='RA')[:1]
        return context

# ----------------
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/detail.html'

    def get_object(self):
        # جلب رابط واحد
        object = super(MovieDetailView, self).get_object()
        # عند مشاعدة التفاصيل يزيد المشاهدة بمقدار واحد
        object.views_count += 1
        object.save()
        return object
    
    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        # فلترة الروابط بالاسم والمقصود اسم الفيلم
        context['links'] = Movie_Links.objects.filter(movie=self.get_object())
        context['related'] = Movie.objects.filter(category=self.get_object().category)[:6]
        return context
    

class MovieCategory(ListView):
    model = Movie
    paginate_by = 2
    template_name = 'movie/list.html'

    def get_queryset(self):
        # متغير عديد به الجاتيجوري
        self.category = self.kwargs['category']
        # فالتر بالاسم
        movies = Movie.objects.filter(category=self.category)
        return movies

    def get_context_data(self, **kwargs):
        # هات كل الافلام اللي فيها الجاتيجوري دي 
        context = super(MovieCategory, self).get_context_data(**kwargs)
        # ورجعها في المتغير ده
        context['movie_category'] = self.category
        return context
    


# -------------------
class MovieLanguage(ListView):
    model = Movie
    paginate_by = 2
    template_name = 'movie/list.html'

    def get_queryset(self):
        # متغير عديد به الجاتيجوري
        self.language = self.kwargs['language']
        # فالتر بالاسم
        movies = Movie.objects.filter(language=self.language)
        return movies

    def get_context_data(self, **kwargs):
        # هات كل الافلام اللي فيها الجاتيجوري دي 
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        # ورجعها في المتغير ده
        context['movie_language'] = self.language
        return context
    

# -------------------
class MovieSearch(ListView):
    model = Movie
    paginate_by = 2
    template_name = 'movie/list.html'

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            list = Movie.objects.filter(title__icontains=search)
        else:
            list = self.model.objects.none()
        return list
    


# ------------------
class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True