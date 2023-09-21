from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Platform(models.Model):
    platform = [
        ("360", "Xbox 360"),
        ("PS3", "Playstaion 3"),
    ]


class Type(models.Model):
    product_type = [
        ("game", "Game"),
        ("console", "Console"),
        ("accessories", "Game"),
    ]


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    platform = models.ForeignKey('Platform', null=True, blank=True, on_delete=models.SET_NULL)
    product_type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
