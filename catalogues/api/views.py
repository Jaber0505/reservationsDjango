from rest_framework import generics
from drf_spectacular.utils import extend_schema

from catalogues.models import Artist
from catalogues.serializers import ArtistSerializer
from catalogues.api.permission import IsAuthenticatedOrReadOnly
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@extend_schema(
    summary="Lister ou créer des artistes",
    description=(
        "Cette vue permet de **consulter la liste des artistes** existants (GET), "
        "ou d'en **créer un nouveau** (POST).\n\n"
        "**HATEOAS activé** : chaque réponse contient un champ `links` avec :\n"
        "- `self` : lien vers la ressource actuelle (GET/PUT/DELETE)\n\n\n"
        "- `all_artists` : lien vers la liste complète\n\n"
        "**Exemple de réponse :**\n"
        "```json\n"
        "{\n"
        "  \"id\": 1,\n"
        "  \"firstname\": \"Amy\",\n"
        "  \"lastname\": \"Winehouse\",\n"
        "  \"links\": {\n"
        "    \"self\": \"/catalogue/api/artists/1/\",\n"
        "    \"all_artists\": \"/catalogue/api/artists/\"\n"
        "  }\n"
        "}\n"
        "```"
    ),
    responses={200: ArtistSerializer, 201: ArtistSerializer}
)
@method_decorator(csrf_protect, name='dispatch')
class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filterset_fields = ['firstname', 'lastname'] 
    ordering_fields = ['firstname', 'lastname']  # 👈 champs autorisés pour le tri
    ordering = ['firstname']

@extend_schema(
    summary="Afficher, modifier ou supprimer un artiste",
    description=(
        "Cette vue permet de :\n"
        "- **Afficher** un artiste via GET `/catalogue/api/artists/{id}/`\n\n\n"
        "- **Mettre à jour** via PUT\n\n\n"
        "- **Supprimer** via DELETE\n\n"
        "Les réponses intègrent le champ `links` avec les liens HATEOAS :\n"
        "- `self` : lien vers cet artiste\n\n\n"
        "- `all_artists` : lien vers la liste complète\n\n"
        "**Exemple de réponse :**\n"
        "```json\n"
        "{\n"
        "  \"id\": 2,\n"
        "  \"firstname\": \"Kurt\",\n"
        "  \"lastname\": \"Cobain\",\n"
        "  \"links\": {\n"
        "    \"self\": \"/catalogue/api/artists/2/\",\n"
        "    \"all_artists\": \"/catalogue/api/artists/\"\n"
        "  }\n"
        "}\n"
        "```"
    ),
    responses={200: ArtistSerializer, 204: None}
)
class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'artist_id'


@method_decorator(csrf_protect, name='dispatch')
class CSRFProtectedPostView(APIView):
    def post(self, request):
        data = request.data
        return Response({'received': data}, status=status.HTTP_201_CREATED)
