from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=20)  
    
    def __str__(self):
        return self.name
    


class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=200,default='',null=True, blank=True)
    image=models.ImageField(upload_to='uploads/products/')


class customer(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    contactNo=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=500)

    
    
   

   
    
