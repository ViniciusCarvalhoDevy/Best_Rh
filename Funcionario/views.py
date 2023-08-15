from django.shortcuts import render, redirect,get_object_or_404
from .forms import Cadastro_Funcionario, Login_Funcionario
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .models import Funcionario

from django.http import HttpResponse
from .models import Funcionario

# Create your views here.
def index(request):
    if request.method =='POST':
        form = Cadastro_Funcionario(request.POST)
        if form.is_valid():
          form.save()
          users = Funcionario.objects.all()
        return render(request,'./Funcionario/cadastro.html',{'form':form,'users':users})
    else:
        form = Cadastro_Funcionario()
        return render(request,'./Funcionario/cadastro.html',{'form':form})

def login_func(request):
  if request.method == 'POST':
    form = Login_Funcionario(request.POST)
  
    if form.is_valid():  
      cd = form.cleaned_data
      print(cd)
      user_auteticate = Funcionario.objects.get(email=cd['email'],password=cd['password'])
      if user_auteticate is not None:
        login(request,user_auteticate)   
        return redirect('home_func')
      return HttpResponse('USER NONE')
    return  HttpResponse('FORMS NOT VALID')
  else:
    form = Login_Funcionario()
    return  render(request,'./Funcionario/login.html',{'form':form})
  
@login_required 
def home(request):
  return render(request,'./Funcionario/home.html')