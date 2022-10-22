from django.urls import path
from .views import MovieListAV, MovieDetailAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie_details')

]