from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #Automatically find querysets from db for us
from .models import Post, Comments
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm
# Create your views here.

#def home(request):
#	return render(request, 'home.html', {})

class homeview(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-id']

class detailview(DetailView):
	model = Post
	template_name = 'article_details.html'

class addpostview(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = ['author', 'title', 'body'] this line isn't required as form class takes care of it

class updatepostview(UpdateView):
	model = Post
	template_name = 'update_post.html'
	fields = ['title', 'body']

class deletepostview(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('homepage')

class commentview(CreateView):
	model = Comments
	form_class = CommentForm
	template_name = 'comments.html'

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

