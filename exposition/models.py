from django.db import models

class Exposition(models.Model):
    nom = models.CharField(max_length=200)  # Nom de l'exposition
    description = models.TextField()  # Description de l'exposition
    date_fabrication = models.DateField()  # Date de fabrication de l'objet exposé
    nom_fabricant = models.CharField(max_length=200)  # Nom du fabricant ou propriétaire
    mots_cles = models.TextField(blank=True, null=True)  # Mots-clés pour la recherche
    image = models.ImageField(upload_to='expositions/', blank=True, null=True)  # Champ pour l'image

    def __str__(self):
        return self.nom
from django.db import models

class Exposition(models.Model):
    nom = models.CharField(max_length=200)  # Nom de l'exposition
    description = models.TextField()  # Description de l'exposition
    date_fabrication = models.DateField()  # Date de fabrication de l'objet exposé
    nom_fabricant = models.CharField(max_length=200)  # Nom du fabricant ou propriétaire
    mots_cles = models.TextField(blank=True, null=True)  # Mots-clés pour la recherche
    image = models.ImageField(upload_to='expositions/', blank=True, null=True)  # Champ pour l'image
    autres_champs_1 = models.CharField(max_length=200, blank=True, null=True)  # Exemple de champ
    autres_champs_2 = models.CharField(max_length=200, blank=True, null=True)  # Exemple de champ

    def __str__(self):
        return self.nom
