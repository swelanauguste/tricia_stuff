from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Ministry


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            Ministry.objects.get_or_create(name=fake.company())

        # with open(f"ministry_list.txt") as file:
        #     for row in file:
        #         name = row.lower().replace("\n", "")
        #         self.stdout.write(self.style.SUCCESS(f"{name} added"))
        #         Ministry.objects.get_or_create(
        #             name=name,
        #         )
        # self.stdout.write(self.style.SUCCESS("list of ministries added"))
