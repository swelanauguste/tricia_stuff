from statistics import mode
from unicodedata import category

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Ministry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'ministries'

    def __str__(self):
        return self.name


class Contract(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateTimeField()
    cost = models.FloatField(default=0)
    contract = models.FileField(upload_to="contracts", blank=True, null=True)

    class Meta:
        ordering = ('end_date',)

    def __str__(self):
        return f"{self.name} from {self.start_date} to {self.end_date} at {self.cost}"
