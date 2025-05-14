from rest_framework import generics
from catalogues.models.representation import Representation
from catalogues.serializers.representation_serializer import RepresentationSerializer

class RepresentationListCreateView(generics.ListCreateAPIView):
    queryset = Representation.objects.all()
    serializer_class = RepresentationSerializer

class RepresentationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Representation.objects.all()
    serializer_class = RepresentationSerializer
