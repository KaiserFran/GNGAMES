from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    foto_perfil = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'nombre', 'apellido', 'foto_perfil', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Quitar todos los help_texts
        for field_name in self.fields:
            self.fields[field_name].help_text = None 