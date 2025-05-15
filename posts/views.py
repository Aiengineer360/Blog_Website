from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category, Tag  # Added Category and Tag models
from .forms import PostForm, CommentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    posts = Post.objects.all()

    # Filtering logic
    query = request.GET.get("q")
    category_slug = request.GET.get("category")
    tag_slug = request.GET.get("tag")
    author_username = request.GET.get("author")

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))

    if category_slug:
        posts = posts.filter(category__slug=category_slug)

    if tag_slug:
        posts = posts.filter(tags__slug=tag_slug)

    if author_username:
        posts = posts.filter(author__username=author_username)

    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'home.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags,
    })

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # Save ManyToMany fields (tags)
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('home')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('home')
    post.delete()
    return redirect('home')
