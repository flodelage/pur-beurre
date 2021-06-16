
from django.core.management.base import BaseCommand
from django.core import management
from django.db import connection

from catalog.utils.populate import Populate


class Command(BaseCommand):
    """
    Command that calls Populate.process() method in order to
    populate the database with some Openfoodfacts' data.
    """

    help = "Populates database with some Openfoodfacts' data"

    def handle(self, *args, **kwargs):
        Populate.process(categories_number=5, pages_number=4)
