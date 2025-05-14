# Permet de générer le groupe Orgnanisateur !
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalogues.models.artist import Artist

class Command(BaseCommand):
    help = 'Crée le groupe Organisateur avec les permissions sur Artist'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Organisateur')
        if created:
            self.stdout.write(self.style.SUCCESS("Groupe 'Organisateur' créé."))
        else:
            self.stdout.write("Groupe 'Organisateur' déjà existant.")

        artist_ct = ContentType.objects.get_for_model(Artist)
        perms = Permission.objects.filter(content_type=artist_ct, codename__in=['change_artist', 'delete_artist'])

        group.permissions.set(perms)
        group.save()

        self.stdout.write(self.style.SUCCESS("Permissions 'change' et 'delete' pour Artist attribuées au groupe 'Organisateur'."))