
import requests
from django.db.utils import IntegrityError

from catalog.utils.exceptions import RequestResponse404
from catalog.models import Category, Product



