
from django.test import TestCase

from catalog.models import Product, Category, Favorite, User


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name='categorie de test')

    def test_name(self):
        category = Category.objects.get(id=1)
        name = category.name
        self.assertEquals(name, 'categorie de test')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_name_unique(self):
        category = Category.objects.get(id=1)
        unique = category._meta.get_field('name').unique
        self.assertEquals(unique, True)

    def test_object_str(self):
        category = Category.objects.get(id=1)
        object_str = category.__str__()
        self.assertEquals(object_str, f"Catégorie {category.pk}: {category.name}")


