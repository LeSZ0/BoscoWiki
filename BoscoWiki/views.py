from django.template import RequestContext
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

def index(request):
	return render(request, 'base/index.html')

def login_page(request):
	message = None

	if not request.user.is_anonymous(): # Si el usuario no tiene una sesion activa
		return redirect('index')

	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username = username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('index')
				else:
					message = "Tu usuario todavia no esta activo"
			else:
				message = "Nombre de usuario o password incorrecto"
	else:
		form = LoginForm()
	return render(request, 'base/login.html', {'message': message, 'form': form})

@login_required(login_url = 'base/login.html')
def logout_page(request):
	logout(request)
	return redirect('index')

@login_required(login_url = 'base/login.html')
def files_page(request):
	return render(request, 'base/archivos.html')