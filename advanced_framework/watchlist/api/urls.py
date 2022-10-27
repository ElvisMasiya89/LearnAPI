from django.urls import path
from .views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetails

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='watchlist_details'),
    path('stream/', StreamPlatformAV.as_view(), name='platform_list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='platform_details'),
    # HyperlinkedModelSerializer url
    path('stream2/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetails.as_view(), name='review-details')


]
