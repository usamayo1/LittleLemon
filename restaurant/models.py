from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateTimeField(auto_now_add=True)
    
class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'