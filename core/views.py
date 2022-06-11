from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

#another way to redirect:
#def index(request):
#	return redirect('/agenda/')

def login_user(request):
	return render(request, 'login.html')

def logout_user(request):
	logout(request)
	return redirect('/')
	
def submit_login(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.error(request, "Invalid username or password.")
	return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
	user = request.user
	evento = Evento.objects.filter(user=user)
	dados = {'eventos':evento}
	return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def event(request):
	return render(request, 'event.html')

@login_required(login_url='/login/')
def submit_event(request):
	if request.POST:
		title = request.POST.get('title')
		event_data = request.POST.get('event_data')
		local = request.POST.get('local')
		description = request.POST.get('description')
		user = request.user
		Evento.objects.create(title=title,
							  event_data=event_data,
							  local=local,
							  description=description,
							  user=user) 
	return redirect('/')
