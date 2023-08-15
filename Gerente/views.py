from django.shortcuts import render, redirect
from .forms import Cadastro_Gerente
from .forms import Login_Gerente
from .models import Gerente
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

rota_tela_cadastro  = './Gerente/cadastro.html'
rota_tela_login  = './Gerente/login.html'

def cadastro_gerente(request):
    form = Cadastro_Gerente
    return render(request=request, template_name=rota_tela_cadastro,context= {'form':form, 'gerentes':buscar_gerentes()})

def salvar_gerente(request): 
    formulario = Cadastro_Gerente (request.POST)   
    if formulario.is_valid():
        formulario.save()      
        form= Cadastro_Gerente     
        return render(request=request, template_name=rota_tela_cadastro, context={'form':form, 'gerentes':buscar_gerentes()})
    else:                 
        form= Cadastro_Gerente       
        return render(request=request, template_name=rota_tela_cadastro, context={'form':form})
    
def buscar_gerentes():
    return  {
        'gerentes': Gerente.objects.all()
    }
    
def logar_gerente(request):
    if request.method == "POST":
        loginForm = Login_Gerente(request.POST)   
        if loginForm.is_valid():    
            email = loginForm.cleaned_data['email']
            senha = loginForm.cleaned_data['password']
            print(email, senha)
            gerente = Gerente.objects.get(email=email,password= senha)
            print(gerente)
            if gerente is not None:
                login(request=request, user=gerente)        
                return redirect('home_gerente')
            else:
                return redirect("login_gerente")
        else: 
            print("Forms não é valido")
            return redirect ("login_gerente")
    return render(request=request,template_name=rota_tela_login, context={'forms':Login_Gerente} )

@login_required(redirect_field_name="login_gerente")
def home_gerente(request):
    return render(request=request,template_name='./Gerente/home.html', context={'gerente':request.user})