from django.db import models

# Modèle représentant un artiste
class Artist(models.Model):
    # Prénom de l'artiste, limité à 60 caractères
    firstname = models.CharField(max_length=60)

    # Nom de famille de l'artiste, limité à 60 caractères
    lastname = models.CharField(max_length=60)

    # Représentation textuelle de l'objet (utile pour l'admin, les logs, etc.)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    # Options supplémentaires du modèle
    class Meta:
        # Nom personnalisé de la table dans la base de données
        db_table = "artists"

        # Permissions personnalisées (peuvent être utilisées avec @permission_required)
        permissions = [
            ("can_delete", "Can delete artist"),  # Permission pour supprimer un artiste
        ]
