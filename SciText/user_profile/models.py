from django.db import models

# Create your models here.
class Users(models.Model):
    # id = models.ForeignKey(max_length=11)
    user_name = models.CharField(max_length=128, verbose_name='User Name')
    login = models.CharField(max_length=128, verbose_name='Login')
    password = models.CharField(max_length=128, verbose_name='Password')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login
