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
from finanzapp.views import index, login_1, register, logout_view, list_transactions, edit_trans, actualizar_trans, delete_trans

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('login/', login_1, name='login'),
    path('register/', register, name='register_user'),
    path('logout/', logout_view, name='logout'),
    path('list/', list_transactions, name='list'),
    path('editTrans/<int:id_transaccion>', edit_trans, name='edit_trans'),
    path('actualizarTrans/<int:id_transaccion>', actualizar_trans, name='actualizar_trans'),
    path('eliminarTrans/<int:id_transaccion>', delete_trans, name='eliminar_trans'),
]
