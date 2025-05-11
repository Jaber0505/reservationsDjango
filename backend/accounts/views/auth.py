from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect

from ..forms import UserSignUpForm

# Vue basée sur une classe pour gérer l'inscription utilisateur
class UserSignUpView(UserPassesTestMixin, CreateView):
    form_class = UserSignUpForm  # Utilise un formulaire personnalisé d'inscription
    success_url = reverse_lazy("login")  # Redirige vers la page de connexion après inscription
    template_name = "registration/signup.html"  # Template utilisé pour le formulaire

    # Vérifie si l'utilisateur a le droit d'accéder à cette page
    def test_func(self):
        # Autorisé uniquement si l'utilisateur est anonyme ou superadmin
        return self.request.user.is_anonymous or self.request.user.is_superuser

    # Redirige avec un message d'erreur si l'utilisateur n'a pas la permission
    def handle_no_permission(self):
        messages.error(self.request, "Vous êtes déjà inscrit!")
        return redirect('home')
