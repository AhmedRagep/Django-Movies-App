from .models import Movie
#
def slider(request):
    # movies = Movie.objects.all().order_by('created')[:1]
    movies = Movie.objects.last()
    return {'slider' : movies}