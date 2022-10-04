from django.core.management.base import BaseCommand

from ...models import Category


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"category_list.txt") as file:
            for row in file:
                name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                Category.objects.get_or_create(
                    name=name,
                )
        self.stdout.write(self.style.SUCCESS("list of categories added"))
