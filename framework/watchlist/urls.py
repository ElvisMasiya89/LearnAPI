from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.movie_view, name='movie_list'),
    path('<int:pk>', views.movie_details_view, name='movie_details')

]
