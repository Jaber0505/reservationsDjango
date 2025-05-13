from django.urls import path
from catalogue.api.views import (
    ArtistListCreateView,
    ArtistRetrieveUpdateDestroyView,
    CSRFProtectedPostView,
)
from catalogue.views.viewIndex import hello_api

urlpatterns = [
    path('artists/', ArtistListCreateView.as_view(), name='artist-list'),
    path('artists/<int:artist_id>/', ArtistRetrieveUpdateDestroyView.as_view(), name='artist-detail'),
    path('test-csrf/', CSRFProtectedPostView.as_view(), name='csrf-test'),
    path('test/', hello_api, name='hello-api'),
]
