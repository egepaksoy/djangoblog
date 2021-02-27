from django.db import models

# Create your models here.


class Post(models.Model):
    img = models.CharField(verbose_name='Fotoğraf Linki', max_length=5000)
    title = models.CharField(verbose_name='Başlık', max_length=200)
    content = models.TextField(verbose_name='Yazı')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
