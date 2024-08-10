from django.db import models



class Category(models.Model):
    cname=models.CharField("Category Name",max_length=20)
    
    def __str__(self):
        return self.cname


class Product(models.Model):
    pname = models.CharField('Product Name', max_length=80)
    category   = models.ForeignKey(Category,   blank=True,   null=True,   on_delete=models.CASCADE)
    author = models.CharField(max_length=30,default="")
    date = models.DateField(auto_now_add=False, null=True)
    price = models.FloatField()
    qty = models.FloatField()
    
    image = models.ImageField(upload_to="productapp",default="")
    
    def __str__(self):
        return self.pname
    
class un(models.Model):
    univer=models.CharField("Category Name",max_length=20)
    
    def __str__(self):
        return self.cname
