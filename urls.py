"""
URL configuration for mainproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from eventorg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.userpage, name="home"),
    path('register', views.register1, name="register"),
    path('login',views.login, name="login"),
    path('userfilldetails',views.filldetails, name="userfilldetails"),
    path('dashboard',views.dashboard, name="Dashboard"),
    path('Visible/',views.formShow,name='visible'),
    path('Tableau/<str:user_id>',views.Tableau,name='Tableau'),
    path('logout',views.logout, name='logout'),
    path('update_status/<int:user_id>/', views.update_status, name='update_status'),
    path('catalog',views.catelog, name="weddcatalog"),
    path('birthday-catalog',views.bircatelog, name="bircatalog"),
    path('org-catalog',views.orgcatalog, name="orgcatalog"),
    path('success',views.success,name="success"),
]
