from django import forms
from django.contrib.auth.models import User

# Formulaire pour modifier les infos de profil (username et email)
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")
