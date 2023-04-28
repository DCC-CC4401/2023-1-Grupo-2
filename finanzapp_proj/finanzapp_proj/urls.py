"""
URL configuration for finanzapp_proj project.

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
from finanzapp.views import login1, logeado, register_user, logout_view, main, list_transactions, edit_trans

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', login1, name='login'),
    path('logeado/', logeado, name='logeado'),
    path('register/', register_user, name='register_user'),
    path('logout/', logout_view, name='logout'),
    path('main/', main, name='main'),
    path('list/', list_transactions, name='list'),
    path('editTrans/<int:id_transaccion>', edit_trans, name='edit_trans'),
]
