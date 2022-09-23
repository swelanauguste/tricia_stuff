from django.contrib import admin

from .models import Category, Ministry, Contract

admin.site.register(Category)
admin.site.register(Ministry)
admin.site.register(Contract)