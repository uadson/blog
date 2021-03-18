from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect


# Create your views here.


def post_list(request):
    posts = Post.objects.filter(
        data_publicacao__lte=timezone.now()).order_by('-data_publicacao')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
    else:
        form = PostForm()

    if form.is_valid():
        post = form.save(commit=False)
        post.autor = request.user
        post.data_publicacao = timezone.now()
        post.save()
        return redirect('blog:post_detail', pk = post.pk)

    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk = pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk = post.pk)
        
    else:
        form = PostForm(instance=post)
        
    return render(request, 'blog/post_edit.html', {'form': form})