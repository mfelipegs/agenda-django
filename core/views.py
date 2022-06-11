from django.shortcuts import render #, redirect
from core.models import Evento
# Create your views here.

#another way to redirect:
#def index(request):
#	return redirect('/agenda/')

def lista_eventos(request):
	user = request.user
	evento = Evento.objects.filter(user=user)
	dados = {'eventos':evento}
	return render(request, 'agenda.html', dados)
