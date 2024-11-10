"""reservations.catalogue URL Configuration
"""
from django.urls import path
from django.contrib import admin

from . import views
from .models import Artist

# Register your models here.
admin.site.register(Artist)

app_name='catalogue'

urlpatterns = [
    path('artist/', views.artist.index, name='artist-index'),
    path('artist/<int:artist_id>', views.artist.show, name='artist-show'),
    path('artist/edit/<int:artist_id>', views.artist.edit, name='artist-edit'),
    path('artist/create/', views.artist.create, name='artist-create'),
    path('artist/delete/<int:artist_id>', views.artist.delete, name='artist-delete'),
]

