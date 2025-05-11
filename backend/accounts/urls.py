from django.urls import path

from .views import UserSignUpView, profile, UserUpdateView, delete_user

app_name = 'accounts'

urlpatterns = [
    path("signup/", UserSignUpView.as_view(), name="user-signup"),
    path("profile/", profile, name="user-profile"),
    path("profile/<int:pk>/", UserUpdateView.as_view(), name="user-update"),
    path("profile/delete/<int:user_id>/", delete_user, name="user-delete"),
]