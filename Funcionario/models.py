from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Funcionario(User):
    cargo = models.TextField(max_length=100)
    salario = models.FloatField()

class Folha_Pagamento(models.Model):
    FK_funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE, default=None)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    pagamento_liquido = models.FloatField()
    
    
