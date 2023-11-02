from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    CAT=((1,'Shoes'),(2,'Sandals'),(3,'Flip Flops'),(4,'Crocs'))
    name=models.CharField(max_length=50,verbose_name='Product Name')
    price=models.FloatField()
    cat=models.IntegerField(verbose_name='Category',choices=CAT)
    pdetail=models.CharField(max_length=300,verbose_name='Product Detail')
    pimage=models.ImageField(upload_to='image')
    is_active=models.BooleanField(default=True)
    '''
    def __str__(self):
        return self.name
        '''
    
class Cart(models.Model):
    userid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    pid=models.ForeignKey('Products',on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

class Order(models.Model):
    orderid=models.CharField(max_length=50)
    userid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    pid=models.ForeignKey('Products',on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)
    amt=models.FloatField()

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()

    def __str__(self):
        return self.name




