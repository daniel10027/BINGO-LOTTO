from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#class pour les models des posts

class Post(models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField()
    datepost = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

#class pour les models de tiquets

class Tiquet(models.Model):
    Lotterie = models.CharField(max_length=150,blank=True)
    recu = models.ForeignKey(User, on_delete=models.CASCADE)
    numero1 = models.IntegerField()
    numero2 = models.IntegerField()
    mise = models.IntegerField()
    datepari =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Lotterie

    def get_absolute_url(self):
        return reverse('pari-detail', kwargs={'pk': self.pk})

#class pour la creation de lotterie

class Lotterie(models.Model):
    nom = models.CharField(max_length=150,blank=True)
    description = models.TextField(default='Entrer la description Ici')
    ouverture = models.DateTimeField(default=timezone.now)
    fermeture = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nom

#class pour la creation des resultats

class Resultat(models.Model):
    nom = models.CharField(max_length=150,blank=True)
    description = models.TextField(default='Entrer la description Ici')
    ouverture = models.DateTimeField(default=timezone.now)
    fermeture = models.DateTimeField(default=timezone.now)
    numero_gagnat = models.CharField(max_length=150,blank=True)
    
    def __str__(self):
        return self.nom


