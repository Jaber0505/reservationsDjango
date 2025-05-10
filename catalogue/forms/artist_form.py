from django import forms

from catalogue.models.artist import Artist
from catalogue.models.type import Type

class ArtistForm(forms.ModelForm):
    # Champ ManyToMany pour sélectionner plusieurs types d'artistes
    types = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Utilisation de cases à cocher
        required=False  # Si tu veux que ce ne soit pas obligatoire
    )

    class Meta:
        model = Artist
        fields = ['firstname', 'lastname', 'types']
