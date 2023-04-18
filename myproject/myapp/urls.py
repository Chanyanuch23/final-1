from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='Home'),
    path('login/', views.login_view,name='Login'),
    path('reg/', views.reg_view, name='Reg')
]