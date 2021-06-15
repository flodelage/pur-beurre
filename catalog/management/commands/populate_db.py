
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
        # with connection.cursor() as cursor:
        #     cursor.execute("DROP SCHEMA public CASCADE;")
        #     cursor.execute("CREATE SCHEMA public;")
        # management.call_command('migrate')
        Populate.process(categories_number=5, pages_number=4)
