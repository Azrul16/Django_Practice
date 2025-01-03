from rest_framework.response import Response
from rest_framework.decorators import api_view
from listitem_app.models import Movie
from .serializers import MovieSerializers

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializers(movie)
    return Response(serializer.data)