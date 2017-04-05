from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Apps.post.models import Post, Category
from Apps.comment.models import Comment
from Apps.post.forms import PostForm

from django.contrib.auth.decorators import login_required, permission_required

def paginate(request, lists, cant_per_page):
	paginator = Paginator(lists, cant_per_page) # Nos mostrará 5 resultados por página

	page = request.GET.get('page')
	try:
		paginat = paginator.page(page)
	except PageNotAnInteger:
		paginat = paginator.page(1)
	except EmptyPage:
		paginat = paginator.page(paginator.num_pages)

	return paginat

# Create your views here.
def index_post(request):
	posts_list = Post.objects.all().order_by('-created_at')
	cant_p_p = 5
	posts = paginate(request, posts_list, cant_p_p)
	return render(request, 'index_post.html', { 'posts': posts} )


@login_required(login_url = '/login')
def create_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
		return redirect('post:index_post')

	else:
		form = PostForm()

	return render(request, 'form_post.html', { 'form': form })

@login_required(login_url = 'login')
def update_post(request, id_post):
	post = Post.objects.get(id = id_post)
	if request.method == 'GET':
		form = PostForm(instance = post)
	else:
		form = PostForm(request.POST, request.FILES ,instance = post)
		if form.is_valid():
			form.save()
		return redirect('post:index_post')

	return render(request, 'edit_post.html', { 'form': form })

def get_post_category(request, id_category):
	posts_list = Post.objects.all().filter(id_category = id_category)
	cant_per_page = 5
	posts = paginate(request, posts_list, cant_per_page)
	category = Category.objects.get(id = id_category)
	return render(request, 'post_categories_filter.html', {'posts': posts, 'category': category})

def view_post(request, id_post):
	post = Post.objects.get(id = id_post)
	return render(request, 'view_post.html', {'post': post, 'comments': Comment.objects.filter(id_post = id_post)})

@permission_required('django.auth.delete_post', login_url = 'login')
def delete_post(request, id_post):
	post = Post.objects.get(id = id_post)
	if request.method == 'POST':
		post.delete()
		return redirect('post:index_post')
	return render(request, 'delete_post.html', {'post': post})

def search_post(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''

	posts_list = Post.objects.filter(postTitle__contains = search_text)
	cant_p_p = 5
	posts = paginate(request, posts_list, cant_p_p)

	return render(request, 'search_post.html', { 'posts': posts} )


class updatePost(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'form_post.html'
	success_url = reverse_lazy('post:list_user')

class deletePost(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('post:list_user')

class createPost(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'form_post.html'
	success_url = reverse_lazy('post:index_post')