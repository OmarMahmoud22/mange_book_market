from django.utils.text import slugify
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name
    

class Books(models.Model):

    class Status(models.TextChoices):
        SOLD = 'SOLD' , 'SOLD'
        AVAILABLE = 'AVAILABLE' , 'AVAILABLE'
        RENTAL = 'RENTAL' , 'RENTAL'

    title = models.CharField( max_length=50)
    body = models.TextField(null=True , blank=True)
    author = models.CharField( max_length=50 , null=True , blank=True)
    photo_book = models.ImageField( upload_to='%y/%m/%d/image_book', null=True , blank=True)
    photo_author = models.ImageField( upload_to='%y/%m/%d/image_author', null=True , blank=True)
    pages = models.IntegerField(null=True , blank=True)
    price = models.DecimalField( max_digits=5, decimal_places=2 ,null=True , blank=True)
    rental_price_day = models.DecimalField( max_digits=5, decimal_places=2 ,null=True , blank=True)
    rental_period = models.IntegerField(null=True , blank=True)
    total_rental = models.DecimalField( max_digits=5, decimal_places=2 ,null=True , blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField( max_length=50 ,choices=Status.choices , default=Status.AVAILABLE )
    category = models.ForeignKey(Category,  on_delete=models.PROTECT , null=True , blank=True)
    publish = models.DateTimeField(default=timezone.now)
    
    
    slug = models.SlugField(max_length=255, unique=True,  blank=True)


    class Meta:
        ordering=['-publish']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detalis', args=[
                                                
                                                self.publish.year,
                                                self.publish.month,
                                                self.publish.day,
                                                self.slug,

                                                ])
    def save(self, *args, **kwargs):
        #*args and **kwargs allow the method to accept any 
        # number of additional arguments and keyword arguments, 
        # which can be passed to the super().save() method.
        if not self.slug:
            # Generate a slug from the title if it doesn't exist
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)