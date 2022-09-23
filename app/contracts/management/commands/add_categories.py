import decimal
import random

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker

CATEGORIES = [
    "server hosting",
    "maintenance",
]


class Provider(faker.providers.BaseProvider):
    def contract_categories(self):
        return self.random_element(CATEGORIES)


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()

        fake.add_provider(Provider)

        print(faker.contract_categories())
