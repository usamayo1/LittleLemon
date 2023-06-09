from django.shortcuts import render
from .models import Menu, Booking
from django.contrib.auth.models import User

# Create your views here.

def HomePage(request):
    return render(request, 'index.html')




# Create Api views here

from .serializers import MenuSerializer, BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .paginations import MyPagination
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.filters import SearchFilter



class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    pagination_class = MyPagination
    
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    filter_backends = [SearchFilter]
    search_fields = ['^title']

class MenuSingleItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class BookingviewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

    
    