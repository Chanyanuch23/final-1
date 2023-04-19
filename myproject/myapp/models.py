from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('TO','Top'),
    ('SK','Skirt'),
    ('PA','Pants'),
    ('SH','Shorts'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    dascrition = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.titli