# catalogues/api/artist_view.py
from rest_framework import generics, permissions
from catalogues.models.artist import Artist
from catalogues.serializers.artist_serializer import ArtistSerializer
from catalogues.permissions.is_organisateur_or_admin import IsOrganisateurOrAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ArtistListCreateView(generics.ListCreateAPIView):
    """
    - Affiche la liste des artistes (requiert d'être connecté)
    - Permet la création d'un artiste si on est Organisateur ou Admin
    """
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsOrganisateurOrAdminOrReadOnly()]


class ArtistDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour afficher, modifier ou supprimer un artiste.
    - Affichage si connecté
    - Modif/Suppression : Organisateur ou Admin
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsOrganisateurOrAdminOrReadOnly()]