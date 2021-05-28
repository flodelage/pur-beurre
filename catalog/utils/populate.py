
import requests
from django.db.utils import IntegrityError

from catalog.utils.exceptions import RequestResponse404
from catalog.models import Category, Product


class Populate():
    """
    Responsability: Requests Openfoodfacts API in order to
    retrieve some categories and their products.
    Then insert them in database.
    """

    def __init__(self):
        """
        Stores categories inserted in database in order know
        which products from wich category have to be inserted
        """
        self.categories_list = []

    def insert_categories(self, categories_number):
        """
        Insert a list of X categories in database
        from Openfoodfacts categories Json
        """
        request = requests.request("GET", "https://fr.openfoodfacts.org/categories.json")
        if request.status_code == 404:
            raise RequestResponse404
        categories_json = request.json()

        for category in categories_json["tags"]:
            category = Category(name=category["name"])
            self.categories_list.append(category)
            if len(self.categories_list) == categories_number:
                break
        Category.objects.bulk_create(self.categories_list)

    def is_product_name_valid(self, product_name):
        """
        Verify that the product name is valid.
        It is only valid if name is not an empty string and:
        - first character is uppercase
          (prevent from names that starts with fr:, en:)
        or
        - first character is a stringified number
          (some names starts with numbers, ex: 100 % pur jus Multifruits)
        """
        if product_name != "":
            if product_name.strip()[0].isupper():
                return True
            elif product_name.strip()[0] in [str(num) for num in range(10)]:
                return True
            else:
                return False
        else:
            return False

    def insert_products(self, pages_number):
        """
        Insert X pages of products from each category in database
        Products are inserted with their categories
        """
        for category in self.categories_list:
            for page in range(pages_number+1):
                request = requests.request("GET", f"https://fr.openfoodfacts.org/categorie/{category.name}.json/{page}")
                if request.status_code == 404:
                    raise RequestResponse404
                products_json = request.json()

                for product in products_json["products"]:
                    try:
                        if self.is_product_name_valid(product["product_name_fr"]):
                            try:
                                Product.objects.create(
                                    name=product["product_name_fr"].strip(),
                                    nutriscore=product["nutriscore_grade"].upper(),
                                    brand=product["brands"],
                                    description=product["generic_name_fr"],
                                    picture=product["image_url"],
                                    url=product["url"]
                                )

                                last_product = Product.objects.latest("id")

                                for cat in product["categories"].split(","):
                                    try:
                                        last_product.categories.add(Category.objects.get(name=cat))
                                    except Category.DoesNotExist:
                                        continue
                                last_product.save()
                            except (KeyError, IntegrityError):
                                continue
                    except KeyError:
                        continue

    def process(self):
        """
        Insert categories and products in database
        """
        self.insert_categories(categories_number=10)
        self.insert_products(pages_number=4)
