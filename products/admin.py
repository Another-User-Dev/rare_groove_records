from django.contrib import admin
from .models import Product, Category, Genre, Rating, Format

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Format)
