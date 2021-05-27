
from django.core.management.base import BaseCommand
from catalog.utils.populate import Populate


class Command(BaseCommand):
    help = 'Populates database'

    def handle(self, *args, **kwargs):
        p = Populate()
        p.process()