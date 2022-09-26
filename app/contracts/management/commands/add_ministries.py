import decimal
import random

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Ministry

# CATEGORIES = [
#     "health",
#     "public service",
#     "treasury",
# ]


# class Provider(faker.providers.BaseProvider):
#     def contract_categories(self):
#         return self.random_element(CATEGORIES)


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # fake.add_provider(Provider)

        for _ in range(17):
            Ministry.objects.get_or_create(name=fake.company())
