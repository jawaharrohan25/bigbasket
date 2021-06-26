from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Receiver(models.Model):
    recname= models.CharField(max_length=50,blank=True,null=False)
    address= models.CharField(max_length=256,blank=True,null=False)
    phone= models.CharField(max_length=10,blank=True,null=False)

    def __str__(self):
        return self.recname

class Product(models.Model):
    pname= models.CharField(max_length=256)
    category= models.ForeignKey("Category",on_delete=models.CASCADE)
    ppic= models.ImageField(upload_to="product_images",null=True)
    price= models.PositiveIntegerField()
    amount= models.CharField(max_length=20)

    def __str__(self):
        return self.pname

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})
    
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={"slug": self.slug})
    

class Category(models.Model):
    cname= models.CharField(max_length=256)
    cpic= models.ImageField(upload_to="category_images",null=True,blank=True)
    slug= models.SlugField()

    def __str__(self):
        return self.cname

class Cart(models.Model):
    product= models.ForeignKey("Product",on_delete=models.CASCADE, null=True)
    customer= models.ForeignKey("auth.User",on_delete=models.CASCADE, null=True)
    qty= models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.product.pname)+' '+str(self.customer)

    def finalprice(self):
        return self.product.price*self.qty

class Order(models.Model):
    customer= models.ForeignKey("auth.user", on_delete=models.CASCADE, null=True)
    receiver= models.ForeignKey("Receiver",on_delete=models.CASCADE,null=True)
    order_date= models.DateField(null=True) 
    arrival_date= models.DateField(null=True)

    def __str__(self):
        return str(self.pk)

class OrderItem(models.Model):
    order= models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    product= models.ForeignKey("Product", on_delete=models.CASCADE, null=True)
    qty= models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.order.pk)+' '+self.product.pname

    def finalprice(self):
        return self.product.price*self.qty
# class ProductCustomer(models.Model):
#     product= models.ForeignKey("Product",on_delete=models.CASCADE)
#     customer= models.ForeignKey("Customer",on_delete=models.CASCADE)
#     qty= models.PositiveIntegerField(default=0)

#     def __str__(self):
#         return self.product.pname
