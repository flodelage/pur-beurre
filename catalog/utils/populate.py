
import requests
from django.db.utils import IntegrityError

from catalog.utils.exceptions import RequestResponse404
from catalog.models import Category, Product


class Populate():

    def __init__(self):
        self.categories_list =[]

    def insert_categories(self, categories_number):
        # requete sur les catégories
        request = requests.request("GET", "https://fr.openfoodfacts.org/categories.json")
        if request.status_code == 404:
            raise RequestResponse404
        categories_json = request.json()

        # pour chacune des X premières categories:
        for category in categories_json["tags"]:
            # je crée une instance de Category et je l'ajoute à la liste
            category = Category(name=category["name"])
            self.categories_list.append(category)
            if len(self.categories_list) == categories_number:
                break
        # j'insère la liste d'instances de Category en bdd
        Category.objects.bulk_create(self.categories_list)

    def insert_products(self, pages_number):
        # pour chacune des X premières pages de la requete sur la categorie:
        for category in self.categories_list:
            for page in range(pages_number+1):
                request = requests.request("GET", f"https://fr.openfoodfacts.org/categorie/{category.name}.json/{page}")
                if request.status_code == 404:
                    raise RequestResponse404
                products_json = request.json()
                # pour chacuns des produits:
                for product in products_json["products"]:
                    # j'essaie d'insérer le produit en bdd
                    try:
                        Product.objects.create(
                            name=product["product_name_fr"],
                            nutriscore=product["nutriscore_grade"].upper(),
                            brand=product["brands"],
                            description=product["generic_name_fr"],
                            picture=product["image_url"],
                            url=product["url"]
                        )
                    except (KeyError, IntegrityError):
                        continue

                    last_product = Product.objects.latest("id")
                    # pour chacune des catégories du produit:
                    for cat in product["categories"].split(","):
                        # j'essaie de la retrouver dans la base de données puis je l'ajoute au produit
                        try:
                            last_product.categories.add(Category.objects.get(name=cat))
                        # si la catégorie n'a pas été enregistrée on continue
                        except Category.DoesNotExist:
                            continue
                    last_product.save()

    def process(self):
        self.insert_categories(categories_number=30)
        self.insert_products(pages_number=4)
