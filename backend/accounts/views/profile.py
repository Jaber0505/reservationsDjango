from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

from ..forms import UserUpdateForm

# Vue basée sur une classe pour modifier les informations de l'utilisateur
class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User  # Modèle à modifier
    form_class = UserUpdateForm  # Formulaire utilisé pour la mise à jour
    template_name = "user/edit.html"  # Template affiché
    success_url = reverse_lazy("accounts:user-profile")  # Redirection après modification

    # Autorise uniquement si l'utilisateur modifie son propre profil
    def test_func(self):
        return self.request.user.pk == self.kwargs["pk"]

# Vue fonctionnelle pour afficher le profil utilisateur
@login_required
def profile(request):
    return render(request, "user/profile.html", {
        "user": request.user  # Envoie l'utilisateur connecté au template
    })

# Vue fonctionnelle pour supprimer le compte utilisateur
@login_required
def delete_user(request, user_id):
    # Vérifie que l'utilisateur existe
    user = get_object_or_404(User, pk=user_id)

    # Empêche un utilisateur de supprimer un autre utilisateur
    if request.user.pk != user.pk:
        return redirect("accounts:user-profile")

    # Supprime le compte uniquement si la requête est en POST
    if request.method == "POST":
        user.delete()
        return redirect("home")

    # Redirige si la méthode HTTP n'est pas autorisée
    return redirect("accounts:user-profile")
