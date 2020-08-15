from rest_framework import serializers
from api.accounts.models import EmailInputModel,RegisterModel


class EmailInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailInputModel
        fields = ['email']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterModel
        field = ['email','otp']