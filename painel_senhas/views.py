from django.shortcuts import render
from.models import StatusSenha, Senha
from django.http import Http404

def index(request):
    try:
        status = StatusSenha.objects.get(nome='Na fila')
    except:
        raise Http404('Status não encontrado')
    senhas = Senha.objects.filter(fk_status_senha=status.id_status_senha)
    return render(request, 'index.html', {'senhas': senhas})
# Create your views here.
