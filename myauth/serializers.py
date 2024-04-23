from myauth.models import Category,Product
from rest_framework import serializers



class Product_serializer(serializers.ModelSerializer):
  

   class Meta:
      model=Product
      fields=['id','name_of_product','price','category']   

class Category_serializer(serializers.ModelSerializer):
   
   class Meta:
      model=Category
      fields=['id','name']         
  