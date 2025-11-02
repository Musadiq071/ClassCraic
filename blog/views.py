from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

# Function-based home view
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# List of all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


# List of posts by specific user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(auhtor=user).order_by('-date_posted')


# Post detail view with likes & comments context
class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.order_by('-date_posted')
        context['total_likes'] = post.likes.count()
        context['liked'] = False
        if self.request.user.is_authenticated:
            context['liked'] = post.likes.filter(id=self.request.user.id).exists()
        return context

    def post(self, request, *args, **kwargs):
        """Handle comment submission from the detail view."""
        post = self.get_object()
        content = request.POST.get('comment')
        if content and request.user.is_authenticated:
            Comment.objects.create(post=post, auhtor=request.user, content=content)
        return redirect('post-detail', pk=post.pk)


# Create post view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'attachment']

    def form_valid(self, form):
        form.instance.auhtor = self.request.user
        # Validate file
        file = form.cleaned_data.get('attachment')
        if file:
            max_size = 5 * 1024 * 1024
            if file.size > max_size:
                form.add_error('attachment', 'File must be under 5MB.')
                return self.form_invalid(form)
            if not (file.name.lower().endswith(('.jpg', '.jpeg', '.png', '.pdf'))):
                form.add_error('attachment', 'Only images or PDFs allowed.')
                return self.form_invalid(form)
        return super().form_valid(form)


# Update post view
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'attachment']
    template_name = 'blog/post_update_form.html'

    def form_valid(self, form):
        form.instance.auhtor = self.request.user
        file = form.cleaned_data.get('attachment')
        if file:
            max_size = 5 * 1024 * 1024
            if file.size > max_size:
                form.add_error('attachment', 'File must be under 5MB.')
                return self.form_invalid(form)
            if not (file.name.lower().endswith(('.jpg', '.jpeg', '.png', '.pdf'))):
                form.add_error('attachment', 'Only images or PDFs allowed.')
                return self.form_invalid(form)
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.auhtor


# Delete post view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.auhtor


# Like/unlike post
@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post-detail', pk=pk)


# Add comment to post
@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        content = request.POST.get('comment')
        if content:
            Comment.objects.create(post=post, auhtor=request.user, content=content)
    return redirect('post-detail', pk=pk)

#Delete a comment
@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    if comment.auhtor == request.user:
        comment.delete()
    return redirect('post-detail', pk=post_pk)

#About page
def about(request):
    return render(request, 'blog/about.html', {
        'title': 'About',
        'description': (
            "Welcome to our Django Blog App! "
            "This app allows users to create posts, like and comment on them. "
            "We used Django, Bootstrap, and Crispy Forms to make it responsive and user-friendly. "
            "Future plans include adding notifications, real-time updates, and user profiles customization."
        ),
        'author': 'Your Name',
    })



# Profile page
def profile(request):
    return render(request, 'users/profile.html')
