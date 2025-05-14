# Droit a donner pour les admin (delete/Update) et authentifier (get)
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Autorise la lecture à tous, mais l'écriture seulement aux admins.
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_staff
