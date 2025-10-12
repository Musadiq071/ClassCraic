from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import (ListView,
 DetailView,
 CreateView,
 UpdateView,
 DeleteView,
 )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post 
# Create your views here.

###There are two types of views 
#1 class views 
# 2 func based views 
# posts = [
	
	
# 	{
# 	'auhtor': 'Musa',
# 	'title':'blog post1',
# 	'content':'second post content',
# 	'date_posted':'August 28, 2025'

# 	},

# 	{
# 	'author': 'yoko',
# 	'title':'blog post2', 
# 	'content':'second post content',
# 	'date_posted':'August 29, 2025'

# 	}
# ]

#func based views 
def home(LoginRequiredMixin):
	context = {
	'posts': Post.objects.all()
	}
	return render(request , 'blog/home.html', context)

class PostListView(ListView):
	model = Post 
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 2
	#<app>/<model>_<viewtype>.html
	#ideal naming convention --> blog/post_list.html


class UserPostListView(ListView):
	model = Post 
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 2
	#<app>/<model>_<viewtype>.html
	#ideal naming convention --> blog/post_list.html

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(auhtor=user).order_by('-date_posted')




class PostDetailView(DetailView):
	model  = Post
	
class PostCreateView(LoginRequiredMixin ,CreateView):
	model  = Post
	fields = ['title', 'content' ]

	def form_valid(self, form):
		form.instance.auhtor  = self.request.user
		return super().form_valid(form)

	
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
	model  = Post
	fields = ['title', 'content' ]

	def form_valid(self, form):
		form.instance.auhtor  = self.request.user
		return super().form_valid(form)
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.auhtor:
			return True
		return False
	
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model  = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.auhtor:
			return True
		return False
	



def about(request):
	return render(request , 'blog/home.html', {'title':'About'})

def profile(request):
	return render(request, 'users/profile.html')