from django.urls import path

from .views import *

app_name = 'catalogue'

urlpatterns = [
    path('artist/', artist.index, name='artist-index'),
    path('artist/<int:artist_id>', artist.show, name='artist-show'),
    path('artist/<int:artist_id>/edit', artist.edit, name='artist-edit'),
    path('artist/<int:artist_id>/delete', artist.delete, name='artist-delete'),
    path('artist/create', artist.create, name='artist-create'),

    path('type/', type.index, name='type-index'),
    path('type/<int:type_id>', type.show, name='type-show'),

    path('locality/', locality.index, name='locality-index'),
    path('locality/<int:locality_id>', locality.show, name='locality-show'),

    path('price/', price.index, name='price-index'),
    path('price/<int:price_id>', price.show, name='price-show'),
]
