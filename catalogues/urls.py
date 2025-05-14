from django.urls import path, include

urlpatterns = [
    path("api/", include(("catalogues.api.urls"), namespace="catalogues_api")),
]