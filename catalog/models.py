
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"Catégorie {self.pk}: {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    nutriscore = models.CharField(max_length=1)
    brand = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.URLField()
    url = models.URLField()
    # Foreign Key(s):
    categories = models.ManyToManyField(Category, related_name="products")

    def __str__(self):
        return f"Produit {self.pk}: {self.name} / Nutriscore: {self.nutriscore} / Marque(s): {self.brand} / Url: {self.url}"


class Favorite(models.Model):
    # Foreign Key(s):
    substitute = models.ForeignKey(Product, related_name="favorites_as_substitute", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="favorites_as_product", on_delete=models.CASCADE)
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Favori {self.pk}: Substitut: {self.substitute} / Produit substitué: {self.product} / Profil: {self.profile}"


class Profile(AbstractUser):
    email = models.EmailField(unique=True, error_messages={'unique': 'A profile with that email already exists.'}, max_length=254)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"Profil {self.pk}: {self.email}"
