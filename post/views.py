from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from post.models import Post
from .forms import PostForm
from user.models import User

# Create your views here.
# TODO kullanıcı girişi yapılcak


def home(request):
    user = get_object_or_404(User, id=1)
    logedin = user.log
    context = {
        "posts": Post.objects.all(),
        "log": logedin
    }
    return render(request, 'home.html', context=context)


def create(request):
    user = get_object_or_404(User, id=1)
    if user.log:
        if request.method == 'POST':
            title = request.POST.get('title')
            img = request.POST.get('img')
            content = request.POST.get('content')
            post = Post(title=title, content=content, img=img)
            post.save()
            return redirect('/')

        else:
            return render(request, 'create.html')
    else:
        return render(request, '404page.html')


def edit(request, id):
    user = get_object_or_404(User, id=1)
    if user.log:
        if request.method == 'POST':
            title = request.POST.get('title')
            img = request.POST.get('img')
            content = request.POST.get('content')
            post = get_object_or_404(Post, id=id)
            post.delete()
            post = Post(title=title, content=content, img=img)
            post.save()
            return redirect('/')

        else:
            post = get_object_or_404(Post, id=id)

            return render(request, 'edit.html', {"post": post})
    else:
        return render(request, '404page.html')


def delete(request, id):
    user = get_object_or_404(User, id=1)
    if user.log:
        post = get_object_or_404(Post, id=id)
        post.delete()
        return redirect('/')
    else:
        render(request, '404page.html')


def post(request, title):
    post = get_object_or_404(Post, title=title)
    return render(request, 'post.html', {"post": post})
