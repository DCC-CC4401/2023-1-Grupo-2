from django import forms

class RegisterUserForm(forms.Form):
   nombre = forms.CharField(label="Nombre de Usuario")
   contraseña = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
   display_name = forms.CharField(label="Apodo")