from django.shortcuts import render
from .models import Menu, Booking
from django.contrib.auth.models import User

# Create your views here.

def HomePage(request):
    return render(request, 'index.html')









# Create Api views here

from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class MenuSingleItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingviewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
# User Registration api
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    