"""ParkingManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('login/', views.login, name='login'),
   path('home/', views.home, name='home'),
   path('testlogin/', views.testlogin, name='testlogin'),
   path('signup/', views.signup, name='signup'),
   path('logout/', views.logout, name='logout'),
   path('spots/',views.spots, name='spots'),
   path('index/',views.index, name='index'),
   path('dashboard/',views.dashboard, name='dashboard'),
   path('sidebar/',views.sidebar, name='sidebar'),
   path('bookslot/',views.bookslot, name='bookslot'),
   path('createslot/',views.createslot, name='createslot'),
   path('searchslot/',views.searchslot, name='searchslot'),
   path('payment/',views.payment, name='payment'),

]