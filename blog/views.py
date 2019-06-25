from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm


def about(request):
    return render(request, 'blog/about.html')

class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/posts.html'
    paginate_by = 10

    def get_queryset(self):
     return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

class PostDetailView(generic.DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = 'title', 'slug', 'text'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = 'title', 'text'

    def form_is_valid(self, form):
        return super().form_valid(form)

@login_required
def drafts(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/drafts.html', {'posts': posts})

@login_required
def post_publish(request, pk, slug):
    post = get_object_or_404(Post, pk=pk, slug=slug)
    post.publish()
    return redirect('post_detail', pk=pk, slug=slug)

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')

def add_comment(request, pk, slug):
    post = get_object_or_404(Post, pk=pk, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk, slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

@login_required
def approve_comment(request, pk, slug):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk, slug=comment.post.slug)

@login_required
def remove_comment(request, pk, slug):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk, slug=comment.post.slug)