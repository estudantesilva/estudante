from django.db import models
from django.utils import timezone 

class StatusSenha(models.Model): 
    id_status_senha = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=255) 

class Categoria(models.Model): 
    id_categoria = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=255) 

class Tipo(models.Model): 
    id_tipo = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=255) 
    
class Senha(models.Model): 
    id_senha = models.AutoField(primary_key=True) 
    fk_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE) 
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    fk_status_senha = models.ForeignKey(StatusSenha, on_delete=models.CASCADE) 
    senha = models.IntegerField() 
    hora_data = models.DateTimeField(default=timezone.now)
