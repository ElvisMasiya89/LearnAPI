from django.contrib import admin
from .models import Movie


# Register your models here.


class WatchlistApp(admin.AdminSite):
    site_header = 'WatchlistApp'


watchlist_app_admin = WatchlistApp(name='watchlist_app_admin')
watchlist_app_admin.register(Movie)
admin.site.register(Movie)