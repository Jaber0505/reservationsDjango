from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('artist/', views.artist.index, name='artist-index'),
    path('artist/<int:artist_id>', views.artist.show, name='artist-show'),
    path('artist/<int:artist_id>/edit', views.artist.edit, name='artist-edit'),
    path('artist/<int:artist_id>/delete', views.artist.delete, name='artist-delete'),
    path('artist/create', views.artist.create, name='artist-create'),
]
