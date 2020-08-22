from rest_framework import serializers
from api.accounts.models import User
from django.core.validators import RegexValidator

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('phone','admin')

class LoginSerializer(serializers.Serializer):

    phone_regex = RegexValidator(regex= r'^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$',message="Phone number must be entered in the format")
    phone = serializers.CharField(validators = [phone_regex],required= True)
    password = serializers.CharField(write_only=True,required=True)

class SignupSerializer(serializers.Serializer):

    phone_regex = RegexValidator(regex= r'^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$',message="Phone number must be entered in the format")
    phone = serializers.CharField(validators = [phone_regex],required= True)
    password1 = serializers.CharField(write_only=True,required=True)
    password2 = serializers.CharField(write_only=True,required=True)

