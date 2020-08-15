from django.db import models

# Create your models here.
class UserModel(models.Model):
    email = models.EmailField( max_length=254)
    otp = models.CharField(unique=True, max_length=6)
    session_timestamp = models.TimeField(auto_now = True)


class EmailInputModel(models.Model):
    email = models.EmailField(unique=True,max_length=254)

class RegisterModel(models.Model):
    email = models.EmailField(unique=True, max_length=254)
    otp = models.IntegerField()