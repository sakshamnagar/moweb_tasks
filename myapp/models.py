from django.db import models
from django.utils.text import slugify

# Create your models here

class NotDel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)
    
class SoftDel(models.Model):
    is_deleted = models.BooleanField(default=False)
    objects = NotDel()              # by changing objects to NotDel, soft-deleted items will not be called
    allobj = models.Manager()       # using allobj, all items which are not hard deleted will be called
    def soft_del(self):             # method to implement soft delete
        self.is_deleted = True
        self.save()
    def restore(self):              # method to restore soft deleted items
        self.is_deleted = False
        self.save()
    class meta:
        abstract = True  


class Vendor(SoftDel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    slug = models.SlugField(max_length=50, default='slug')
    image = models.ImageField(upload_to='image',default='image/image.jpg')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    #method to update the slug field automatically with first & last name before saving
    def save(self,*args,**kwargs):
        full_name = self.first_name + ' ' + self.last_name
        self.slug = slugify(full_name)
        super(Vendor,self).save(*args,**kwargs)


class Fruits(SoftDel):
    vendor_fruits = models.ForeignKey(Vendor,related_name='fruits',on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    
class Vegitables(SoftDel):
    vendor_vegitables = models.ForeignKey(Vendor,related_name='vegitables',on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class Store(SoftDel):
    name = models.CharField(max_length=50)
    vendors = models.ManyToManyField(Vendor)
    def __str__(self):
        return self.name