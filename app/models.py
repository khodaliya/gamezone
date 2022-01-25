from itertools import product
from django.db import models

from app.helpers import generate_slug

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=90)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
CATAGORY_CHOICE = (
    ('GC', 'Gaming Computers'),
    ('GM', 'Gaming Mobile'),
    ('GL', 'Gaming Laptops'),
    ('GMT', 'Gaming Moniter'),
    ('GH', 'Gaming Headphones'),
    ('KM', 'Keybord Mouse'),
)    

class Product(models.Model):
    title = models.CharField(max_length=122,null=True,blank=True)
    p_tag = models.CharField(max_length=300,null=True,blank=True)
    amazon = models.CharField(max_length=500,null=True,blank=True)
    slug = models.SlugField(max_length=122,null=True,blank=True)
    amazon_price = models.CharField(max_length=122,null=True,blank=True)
    flipkart_price = models.CharField(max_length=122,null=True,blank=True)
    catagory = models.CharField(choices=CATAGORY_CHOICE,max_length=3,null=True,blank=True)
    pro_detail = models.TextField()
    content= models.TextField()
    img1 = models.ImageField(upload_to = 'productimg',null=True,blank=True)
    img2 = models.ImageField(upload_to = 'productimg',null=True,blank=True)
    img3 = models.ImageField(upload_to = 'productimg',null=True,blank=True)
    img4 = models.ImageField(upload_to = 'productimg',null=True,blank=True)
    bg_img01 = models.ImageField(upload_to = 'productimg',null=True,blank=True)
    bg_img02 = models.ImageField(upload_to = 'productimg',null=True,blank=True)
    bg_img03 = models.ImageField(upload_to = 'productimg',null=True,blank=True)
    
    def __str__(self):
        return str(self.title)


    def save(self,*args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Product,self).save(*args, **kwargs)
