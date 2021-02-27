from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(verbose_name='Kullanıcı adı', max_length=100)
    password = models.CharField(verbose_name='Şifre', max_length=200)
    log = models.BooleanField(verbose_name='Giriş Yapılmış mı')

    def __str__(self):
        return self.name
