
from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name='shophome'),
    path('about/', views.about, name='about us'),
    path('contact/', views.contact, name='Contact us'),
    path('tracker/', views.tracker, name='trackingstatus'),
    path('search/', views.search, name='search'),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path('checkout/', views.checkout, name='checkout')

]
