from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WatchListAV, WatchListDetailAV, StreamPlatformDetailAV, ReviewList, ReviewDetails, \
    ReviewCreate, StreamPlatformVS

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='stream-platform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='watchlist_details'),

    path('', include(router.urls)),

    # path('stream/', StreamPlatformAV.as_view(), name='platform_list'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='platform_details'),
    # HyperlinkedModelSerializer url

    path('stream2/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetails.as_view(), name='review-details')

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetails.as_view(), name='review-details')
]
