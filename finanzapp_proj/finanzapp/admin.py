from django.contrib import admin

# Register your models here.
from finanzapp.models import  User, Transaction, Category

admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(Category)