import datetime
import random

from django.core.management.base import BaseCommand
from django.forms import FloatField
from faker import Faker

from ...models import Category, Contract, Ministry

def get_cost():
    fake = Faker()
    cost = fake.pricetag().replace("$", "")
    cost = cost.replace(",", "")
    cost = cost.replace(".", '')
    cost= float(cost)
    return cost


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # print(fake.date_between(datetime.date(2022, 9, 1), datetime.date(2022, 9, 3)))

        for _ in range(10):
            Contract.objects.get_or_create(category = Category.objects.get(pk=random.randint(1, 2)),
            ministry = Ministry.objects.get(pk=random.randint(1, 10)),
            name = fake.company(),
            # ministry = fake.company(),
            start_date = fake.date_between(datetime.date(2022, 1, 1)),
            end_date =fake.date_between(datetime.date(2022, 8, 30)),
            cost = get_cost()
            )
