"""problog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post import views as pviews
from user import views as uviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pviews.home),
    path('create/', pviews.create),
    path('delete/<int:id>', pviews.delete),
    path('edit/<int:id>', pviews.edit),
    path('<str:title>', pviews.post),
    path('login/', uviews.login),
    path('login/giris/', uviews.giris),
    path('logout/', uviews.logout),
]
