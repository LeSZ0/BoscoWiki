from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import permission_required, login_required

#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

from Apps.user.forms import UserForm

# from Apps.user.models import User


# Create your views here.

@permission_required('django.auth.index_user', login_url = 'login')
def index_user(request):
	users = User.objects.all().order_by('id')
	return render(request, 'index_user.html', { 'users': users })


def create_user(request):
	if request.method == 'POST':
		datos = {
			'username': request.POST['username'],
			'email': request.POST['email'],
			'password1': request.POST['password1'],
			'password2': request.POST['password2'],
			'first_name': request.POST['first_name'],
			'last_name': request.POST['last_name'],
			'is_active': 0,

		}
		
		form = UserForm(datos)

		if form.is_valid():
			form.save()
		else:
			message = form.errors
			return render(request, 'form_user.html', { 'form': form, 'message': message })

		return redirect('usuario:index_user')

	else:
		form = UserForm()

	return render(request, 'form_user.html', { 'form': form })

@login_required(login_url = 'login')
def update_user(request, id_user):
	user = User.objects.get(id = id_user)
	if request.method == 'GET':
		form = UserForm(instance = user)
	else:
		form = UserForm(request.POST, instance = user)
		if form.is_valid():
			form.save()
		return redirect('usuario:index_user')

	return render(request, 'edit_user.html', { 'form': form })

@permission_required('django.auth.delete_user', login_url = 'login')
def delete_user(request, id_user):
	user = User.objects.get(id = id_user)
	if request.method == 'POST':
		user.delete()
		return redirect('usuario:index_user')

	return render(request, 'delete_user.html', { 'user': user })

@login_required(login_url = 'login')
def view_user(request, id_user):
	user = User.objects.get(id = id_user)
	return render(request, 'view_user.html', {'userr': user})


class listUser(ListView):
	model = User
	template_name = 'list_user.html'

class createUser(CreateView):
	model = User
	form_class = UserForm
	template_name = 'form_user.html'
	success_url = reverse_lazy('usuario:index_user')

class updateUser(UpdateView):
	model = User
	form_class = UserForm
	template_name = 'form_user.html'
	success_url = reverse_lazy('usuario:list_user')

class borrarUser(DeleteView):
	model = User
	template_name = 'delete_user.html'
	success_url = reverse_lazy('usuario:delete_user')

class viewUser(DeleteView):
	model = User
	template_name = 'view_user.html'
	success_url = reverse_lazy('usuario:view_user')