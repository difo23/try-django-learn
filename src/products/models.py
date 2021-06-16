from django.db import models

# Create your models here.

class Product(models.Model):
  title  		= models.CharField( max_length = 120 ) # max_length is required
  desciption 	= models.TextField( blank = True, null = True )
  summary		= models.TextField( default = 'this is cool!' )
  price = models.DecimalField( decimal_places = 2, max_digits = 10000 )
    
