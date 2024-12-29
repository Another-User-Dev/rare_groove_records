from django.contrib import admin
from .models import Product, Category, Genre, Rating, Format

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'category',
        'artist',
        'title',
        'description',
        'genre',
        'format',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'genre',
    )

class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'rating',
    )

class FormatAdmin(admin.ModelAdmin):
    list_display = (
        'format',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Format, FormatAdmin)
