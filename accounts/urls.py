from django.urls import path

from .views import UserSignUpView, profile, UserUpdateView, delete_user
from .api.views import RegisterView, LoginView, CustomTokenObtainPairView
from accounts.views.me import MeView
from accounts.views.change_password import ChangePasswordView
from accounts.views.logout import LogoutView

app_name = 'accounts'

urlpatterns = [
    path("signup/", UserSignUpView.as_view(), name="user-signup"),
    path("profile/", profile, name="user-profile"),
    path("profile/<int:pk>/", UserUpdateView.as_view(), name="user-update"),
    path("profile/delete/<int:user_id>/", delete_user, name="user-delete"),

    path('api/register/', RegisterView.as_view(), name='register'),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),

    path('api/me/', MeView.as_view(), name='me'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]