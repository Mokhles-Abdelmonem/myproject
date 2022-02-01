from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user") , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100,blank=True, null=True)
    first_name = models.CharField('first name', max_length=120,blank=True,null=True)
    last_name = models.CharField('last name', max_length=120,blank=True,null=True)
    email_address = models.EmailField('Email Address', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username