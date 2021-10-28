
from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    email = models.EmailField(unique=True, error_messages={'unique': 'Un utilisateur avec cet email existe déjà.'}, max_length=254)
    username = models.CharField(unique=True, error_messages={'unique': 'Un utilisateur avec ce nom existe déjà.'}, max_length=128)
    password = models.CharField(max_length=128)

    REQUIRED_FIELDS = ['email','password'] # required fields at the creation
    USERNAME_FIELD = 'username' # set as login field / by the way set as required field implicitly

    def __str__(self):
        return f"Profil {self.pk}: {self.username} / {self.email}"
