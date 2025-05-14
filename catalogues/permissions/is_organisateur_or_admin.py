# Les droits pour les organisateurs
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOrganisateurOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        # Pour POST, PUT, DELETE, etc.
        return request.user and request.user.is_authenticated and (
            request.user.is_staff or request.user.groups.filter(name='Organisateur').exists()
        )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        if request.user.is_staff:
            return True
        return request.user.groups.filter(name='Organisateur').exists()
