from django.db import models
from .group import GROUPS
# from .enum import NormalUser
from django.contrib.auth.models import AbstractUser, Group
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    # user_type = models.IntegerField(choices=NormalUser.choices(), default=NormalUser.NORMAL_USER)
    REQUIRED_FIELDS = ['username','phone','first_name','last_name','groups','is_staff']

    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
