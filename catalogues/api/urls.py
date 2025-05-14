from django.urls import path
from catalogues.api import (
    ArtistDetailView, ArtistListCreateView,
    ArtistTypeListCreateView,
    LocalityListCreateView,
    LocationListCreateView,
    PriceShowListCreateView,
    PriceListCreateView,
    PriceDetailView,
    ShowListCreateView,
    ShowDetailView,
    TypeListCreateView,
    TypeDetailView,
    RepresentationListCreateView,
    RepresentationDetailView,
    ReservationRepresentationListCreateView,
    ReservationRepresentationDetailView,
    ReservationListCreateView,
    ReservationDetailView,
    ReviewListCreateView,
    ReviewDetailView,
)

app_name = "catalogues_api"

urlpatterns = [
    # Route -> Artist
    path("artists/", ArtistListCreateView.as_view(), name="artist-list"),
    path("artists/<int:pk>/", ArtistDetailView.as_view(), name="artist-detail"),

    path('artist_types/', ArtistTypeListCreateView.as_view(), name='artist-type-list-create'),
    path('localities/', LocalityListCreateView.as_view(), name='locality-list-create'),
    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('price_shows/', PriceShowListCreateView.as_view(), name='price_show-list-create'),
    path('prices/', PriceListCreateView.as_view(), name='price-list-create'),
    path('prices/<int:pk>/', PriceDetailView.as_view(), name='price-detail'),
    path('shows/', ShowListCreateView.as_view(), name='show-list-create'),
    path('shows/<int:pk>/', ShowDetailView.as_view(), name='show-detail'),
    path('types/', TypeListCreateView.as_view(), name='type-list-create'),
    path('types/<int:pk>/', TypeDetailView.as_view(), name='type-detail'),
    path('representations/', RepresentationListCreateView.as_view(), name='representation-list-create'),
    path('representations/<int:pk>/', RepresentationDetailView.as_view(), name='representation-detail'),
    path('reservation_representations/', ReservationRepresentationListCreateView.as_view(), name='reservation-representation-list-create'),
    path('reservation_representations/<int:pk>/', ReservationRepresentationDetailView.as_view(), name='reservation-representation-detail'),
    path('reservations/', ReservationListCreateView.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]