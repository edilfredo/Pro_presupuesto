from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser
from .models import Presupuesto, ItemPresupuesto
from django.forms import inlineformset_factory

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name','last_name','role', 'password1', 'password2']
        """labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'role': 'Rol en el sistema',
          
        }"""


# Formulario presupuesto
class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = ['nombre', 'unidad', 'cantidad', 'valor_unitario']

class ItemPresupuestoForm(forms.ModelForm):
    class Meta:
        model = ItemPresupuesto
        fields = ['codigo', 'nombre', 'unidad', 'cantidad', 'valor_unitario']

ItemFormSet = inlineformset_factory(
    Presupuesto, ItemPresupuesto, form=ItemPresupuestoForm,
    extra=1, can_delete=True
)
