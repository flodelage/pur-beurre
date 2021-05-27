
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


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(
            name='produit de test',
            nutriscore='C',
            brand='Nestlé',
            description='produit sans gluten',
            picture='https://static.openfoodfacts.org/images/products/1234.jpg',
            url='https://fr.openfoodfacts.org/produit/1234/produit_de_test'
        )

    def test_name(self):
        product = Product.objects.get(id=1)
        name = product.name
        self.assertEquals(name, 'produit de test')

    def test_name_unique(self):
        product = Product.objects.get(id=1)
        unique = product._meta.get_field('name').unique
        self.assertEquals(unique, True)

    def test_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_nutriscore(self):
        product = Product.objects.get(id=1)
        nutriscore = product.nutriscore
        self.assertEquals(nutriscore, 'C')

    def test_nutriscore_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('nutriscore').max_length
        self.assertEquals(max_length, 1)

    def test_brand(self):
        product = Product.objects.get(id=1)
        brand = product.brand
        self.assertEquals(brand, 'Nestlé')

    def test_brand_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('brand').max_length
        self.assertEquals(max_length, 200)

    def test_brand_default(self):
        product = Product.objects.get(id=1)
        default = product._meta.get_field('brand').default
        self.assertEquals(default, 'Non renseigné')

    def test_description(self):
        product = Product.objects.get(id=1)
        description = product.description
        self.assertEquals(description, 'produit sans gluten')

    def test_description_default(self):
        product = Product.objects.get(id=1)
        default = product._meta.get_field('description').default
        self.assertEquals(default, 'Non renseigné')

    def test_picture(self):
        product = Product.objects.get(id=1)
        picture = product.picture
        self.assertEquals(picture, 'https://static.openfoodfacts.org/images/products/1234.jpg')

    def test_picture_default(self):
        product = Product.objects.get(id=1)
        default = product._meta.get_field('picture').default
        self.assertEquals(default, 'Non renseigné')

    def test_url(self):
        product = Product.objects.get(id=1)
        url = product.url
        self.assertEquals(url, 'https://fr.openfoodfacts.org/produit/1234/produit_de_test')

    def test_object_str(self):
        product = Product.objects.get(id=1)
        object_str = product.__str__()
        self.assertEquals(object_str, f"Produit {product.pk}: {product.name} / Nutriscore: {product.nutriscore} / Marque(s): {product.brand} / Url: {product.url}")
