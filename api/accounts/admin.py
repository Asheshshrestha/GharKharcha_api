from django.contrib import admin
from api.accounts.models import EmailInputModel,UserModel

# Register your models here.

admin.site.register(EmailInputModel)
admin.site.register(UserModel)