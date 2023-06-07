from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.HomePage, name='home'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.MenuSingleItemView.as_view(), name='singlemenu'),

]