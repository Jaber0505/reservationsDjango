from django.urls import path

from catalogue import views
from catalogue.api.views import ArtistListCreateView, ArtistRetrieveUpdateDestroyView
from catalogue.api.views import CSRFProtectedPostView

app_name = 'catalogue'

urlpatterns = [
    path('artist/', views.artist.index, name='artist-index'),
    path('artist/<int:artist_id>', views.artist.show, name='artist-show'),
    path('artist/<int:artist_id>/edit', views.artist.edit, name='artist-edit'),
    path('artist/<int:artist_id>/delete', views.artist.delete, name='artist-delete'),
    path('artist/create', views.artist.create, name='artist-create'),

    path('type/', views.type.index, name='type-index'),
    path('type/<int:type_id>', views.type.show, name='type-show'),

    path('locality/', views.locality.index, name='locality-index'),
    path('locality/<int:locality_id>', views.locality.show, name='locality-show'),

    path('price/', views.price.index, name='price-index'),
    path('price/<int:price_id>', views.price.show, name='price-show'),

    path('representation/', views.representation.index, name='representation-index'),
    path('representation/<int:representation_id>/', views.representation.show, name='representation-show'),

    path('reservation/', views.reservation.reservation_index, name='reservation_index'),
    path('reservation/<int:reservation_id>/', views.reservation.reservation_detail, name='reservation_detail'),

    path('location/', views.location.index, name='location-index'),
    path('location/<int:location_id>/', views.location.show, name='location-show'),

    path('show/', views.show_.index, name='show-index'),
    path('show/<int:show_id>/', views.show_.show, name='show-show'),
    path('showdetail/<int:show_id>/', views.show_detail.detail, name='show-detail'),

    path('review/', views.review.index, name='review-index'),
    path('review/<int:review_id>/', views.review.show, name='review-show'),

    #### API ####
    path('api/artists/', ArtistListCreateView.as_view(), name='artist-list'),
    path('api/artists/<int:artist_id>/', ArtistRetrieveUpdateDestroyView.as_view(), name='artist-detail'),

    path('api/test-csrf/', CSRFProtectedPostView.as_view(), name='csrf-test'),
]
