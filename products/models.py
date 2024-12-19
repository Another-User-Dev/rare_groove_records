from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Genre(models.Model):
    genre = models.CharField(max_length=254, null=True, blank=True)    

    def __str__(self):
        return self.genre   


class Rating(models.Model):
    rating = models.PositiveIntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    review_email_addr = models.EmailField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Format(models.Model):
    format = models.CharField(max_length=254, null=True, blank=True)
    friendly_format_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.format

    def get_friendly_format_name(self):
        return self.friendly_format_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    artist = models.CharField(max_length=512, null=True, blank=True)
    title = models.CharField(max_length=512, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    genre = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.ForeignKey('Rating', null=True, blank=True, on_delete=models.SET_NULL)
    format = models.ForeignKey('Format', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

