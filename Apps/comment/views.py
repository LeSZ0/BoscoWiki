from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

from Apps.comment.models import Comment
from Apps.comment.forms import CommentForm

from django.contrib.auth.decorators import login_required, permission_required

def index_comment(request):
	comments = Comment.objects.all().order_by('-created_at')
	return render(request, 'index_comment.html', {'comments': comments})

@login_required(login_url = '/login')
def create_comment(request, id_post):
	if request.method == 'GET':
		comment = CommentForm(request.GET)

		if comment.is_valid():
			comment.save()
		return redirect('post:view_post', id_post)
	else:
		comment = CommentForm()
	return render(request, 'form_comment.html', {'comment': comment, 'post_id': id_post})

#@permission_required(delete_user, login_url = '/url')
def delete_comment(request, id_comment):
	comment = Comment.objects.get(id = id_comment)
	if request.method == 'GET':
		comment.delete()
		return redirect('post:index_post')
	return render(request, 'delete_comment.html', {'comment': comment})
