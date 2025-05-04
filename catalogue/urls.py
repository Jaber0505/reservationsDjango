from django.urls import path

from .views import artist

app_name = 'catalogue'

urlpatterns = [
    path('artist/', artist.index, name='artist-index'),
    path('artist/<int:artist_id>', artist.show, name='artist-show'),
    path('artist/<int:artist_id>/edit', artist.edit, name='artist-edit'),
    path('artist/<int:artist_id>/delete', artist.delete, name='artist-delete'),
    path('artist/create', artist.create, name='artist-create'),
]
