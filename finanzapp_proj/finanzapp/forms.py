from django import forms
from finanzapp.models import Transaction, Category

class RegisterUserForm(forms.Form):
   nombre = forms.CharField(label="Nombre de Usuario")
   contraseña = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
   display_name = forms.CharField(label="Apodo")

class EditTransactionForm(forms.ModelForm):
   class Meta:
      model = Transaction
      fields = ["type", "description", "amount", "date"]

class EditCategoryForm(forms.ModelForm):
   class Meta:
      model = Category
      fields= ["name", "budget"]
