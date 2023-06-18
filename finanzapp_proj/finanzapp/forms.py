from django import forms
from finanzapp.models import Transaction, Category

class RegisterUserForm(forms.Form):
   nombre = forms.CharField(label="Nombre de Usuario")
   contraseña = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
   display_name = forms.CharField(label="Apodo")

class EditTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["type", "description", "amount", "date", "category"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(EditTransactionForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)
        self.fields['category'].label_from_instance = lambda obj: obj.name

class EditCategoryForm(forms.ModelForm):
   class Meta:
      model = Category
      fields= ["name", "budget"]


