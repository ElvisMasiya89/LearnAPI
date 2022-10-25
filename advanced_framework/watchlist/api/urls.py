from django.urls import path
from .views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='watchlist_details'),
    path('stream/', StreamPlatformAV.as_view(), name='platform_list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='platform_details'),


]
