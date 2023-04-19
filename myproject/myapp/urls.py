"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('home/', views.Home, name='Home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('home/', views.Home, name='Home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Home, name='Home'),
    path('about/', views.about, name='about'),
    path('acc/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
    path('product-detail/', views.productdetail, name='productdetail'),
    path('products/', views.products, name='products'),
    path('top/', views.top, name='top'),
    path('logout/', views.logout, name='logout'),
    # path('category/', views.CategoryView.as_view(),name='category'),
    # path('product-detail/<int:pk>', views.Productdetail.as_view(),name='product-detail')
]