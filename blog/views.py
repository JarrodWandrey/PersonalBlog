from django.shortcuts import render, redirect
from django.http import HttpResponse
from .services import get_all_posts, create_post, get_post_by_id, update_post as update_post_service, delete_post as delete_post_service, create_comment
from .forms import CommentForm

# Base view to show all posts
def home(request):
    page_number = request.GET.get('page', 1)
    post_page = get_all_posts(page_number=page_number)

    return render(request, 'home.html', {'posts': post_page})

# View to add a new post
def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        create_post(title, author, content)
        return home(request)
    return render(request, 'add_post.html')

# View to show a single post
def show_post(request, post_id):
    form = CommentForm()
    post = get_post_by_id(post_id)
    if post:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                author = form.cleaned_data['author']
                content = form.cleaned_data['content']
                create_comment(post_id, author, content)
                return redirect('show_post', post_id=post_id)
        return render(request, 'show_post.html', {'post': post, 'form': form})
    else:
        return HttpResponse("Post not found", status=404)

# View to update an existing post
def update_post(request, post_id):
    post = get_post_by_id(post_id)
    if not post:
        return HttpResponse("Post not found", status=404)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        update_post_service(post_id, title, author, content)
        return show_post(request, post_id)
    
    return render(request, 'update_post.html', {'post': post})

# View to delete a post
def delete_post(request, post_id):
    success = delete_post_service(post_id)
    if success:
        return home(request)
    else:
        return HttpResponse("Post not found", status=404)