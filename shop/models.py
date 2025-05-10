from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    product_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

