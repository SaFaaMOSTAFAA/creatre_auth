from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name_of_product=models.CharField(max_length=50)
    price=models.FloatField()    
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_product



    

