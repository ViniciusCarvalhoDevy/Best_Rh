from django import forms
from .models import Funcionario
class Cadastro_Funcionario(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('username','first_name','last_name','email','password','cargo','salario')
        labels = {
            'username' : 'Login',
            'first_name' : None,
            'last_name' : None,
            'email ': None,
            'password' : None,
            'cargo' : None,
            'salario' : None
         }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Digite seu login . . '}),
            'password': forms.PasswordInput(attrs={'placeholder':'Digite uma senha . . '}),
        }
class Login_Funcionario(forms.ModelForm):
    class Meta: 
        model = Funcionario
        fields = ('email','password')
        
        

        
        
     
        
    