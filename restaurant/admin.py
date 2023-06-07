from django.contrib import admin
from .models import Booking, Menu

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'no_of_guests', 'bookingdate']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'inventory']