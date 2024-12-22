from django.urls import path
from . import views

app_name = 'listitem_app'

urlpatterns = [
    path('list/', views.movie_list, name='movie_list'),
    path('<int:pk>', views.movie_details, name='movie-detail'),
    
]