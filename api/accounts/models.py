from __future__ import unicode_literals
import re
from django.db import DefaultConnectionProxy, models 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from django.db.models import Q 
from django.db.models.signals import pre_save,post_save
from library.otp_generator import generateOTP
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class MyUserManager(BaseUserManager):

    def create_user(self,phone,password=None):
        if not phone:
            raise ValueError("Users must have a phone number")
        user = self.model(phone = phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone,password = None):
        user = self.create_user(
            phone=phone,
            password=password
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user
    def create_staffuser(self,phone,password=None):
        user = self.create_user(
            phone=phone,
            password=password
        )
        user.staff = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    phone_regex = RegexValidator(regex= r'^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$',message="Phone number must be entered in the format")
    phone = models.CharField(validators=[phone_regex],max_length=15,unique=True)
    name = models.CharField(max_length=20,blank=True,null=True)
    first_login = models.BooleanField(default=False)
    active = models.BooleanField(_('active'),default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD  = 'phone'
    REQUIRED_FIELDS = []
    
    objects = MyUserManager()

    def __str__(self):
        return self.phone

    @property
    def is_superuser(self):
        return self.admin
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_active(self):
        return self.active

    def has_perm(self,perm,obj=None):
        return self.admin

    def has_module_perms(self,app_label):
        return True


