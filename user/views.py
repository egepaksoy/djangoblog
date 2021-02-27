from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from user.models import User

# Create your views here.
# TODO kullanıcı girişine göre kısımlar gösterilcek root ve gues olarak ayrı iki sayfa


def login(request):
    return render(request, 'login.html')


def giris(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    user = get_object_or_404(User, name=name)
    if user.password == password:
        user.log = True
    else:
        user.log = False
    user.save()
    return redirect('/')


def logout(request):
    user = get_object_or_404(User, id=1)
    user.log = False
    user.save()
    return redirect('/')
