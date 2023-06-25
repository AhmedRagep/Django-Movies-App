from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCategory, MovieLanguage, MovieSearch, MovieYear

app_name='movie'
urlpatterns = [
    path('', MovieListView.as_view(), name='list'),
    path('category/<str:category>', MovieCategory.as_view(), name='category'),
    path('language/<str:language>', MovieLanguage.as_view(), name='language'),
    path('search', MovieSearch.as_view(), name='search'),
    path('year/<int:year>', MovieYear.as_view(), name='year'),
    path('<slug:slug>', MovieDetailView.as_view(), name='detail'),
    
]
