from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import PostForm

# Create your views here.

def index(request):
    return render(request, 'quiz/index.html')

def list(request):
    posts = Post.objects.all

    if request.method == 'post':
        form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('list')
    else:
        form = PostForm()

    return render(request, 'quiz/list.html', {'posts': posts, 'form': form})