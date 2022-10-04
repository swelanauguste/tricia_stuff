from email.policy import default

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"


class Ministry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "ministries"

    def __str__(self):
        return f"{self.name}"


class Contract(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    contract = models.FileField(
        upload_to="contracts", blank=True, null=True, default="default_contract.pdf"
    )

    class Meta:
        ordering = ("-end_date",)

    def get_absolute_url(self):
        return reverse("contracts:contract-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} of ${self.cost}, between {self.start_date} and {self.end_date}"
