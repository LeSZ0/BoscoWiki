from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from Apps.rol.models import Rol
from Apps.rol.forms import RolForm

# Create your views here.
def index_rol(request):
	roles = Rol.objects.all().order_by('id')
	return render(request, 'index_rol.html', { 'roles': roles } )

class updateRol(UpdateView):
	model = Rol
	form_class = RolForm
	template_name = 'form_rol.html'
	success_url = reverse_lazy('rol:index_rol')

class deleteRol(DeleteView):
	model = Rol
	template_name = 'delete_rol.html'
	success_url = reverse_lazy('rol:index_rol')

class createRol(CreateView):
	model = Rol
	form_class = RolForm
	template_name = 'form_rol.html'
	success_url = reverse_lazy('rol:index_rol')