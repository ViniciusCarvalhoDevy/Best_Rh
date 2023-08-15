from django import forms
from .models import Gerente

class Cadastro_Gerente(forms.ModelForm):
    class Meta:
        model = Gerente
        fields = ('username', 'first_name', 'last_name','email', 'password', 'salario')
        
class Login_Gerente(forms.ModelForm):
    class Meta:
        model = Gerente
        fields = ('email', 'password')
        widgets={
            'email': forms.TextInput(attrs={'placeholder':'Digite seu email...' })
        }