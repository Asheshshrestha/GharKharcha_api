from django.shortcuts import render
from api.accounts.serializers import EmailInputSerializer,RegisterSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from library.otp_generator import generateOTP
from api.accounts.models import UserModel
from rest_framework import status
from library.mail_sender import send_single_mail
import os
from gharkharcha.settings import BASE_DIR

# Create your views here.


@csrf_exempt
def register_request(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmailInputSerializer(data = data)
        if serializer.is_valid():
            try:
                email = serializer.data['email']
                
                #user = UserModel.objects.get(email=email)
                #user.delete()

                if(not UserModel.objects.filter(email=email).exists()):
                    otp = generateOTP()
                    user = UserModel(email=email,otp=otp)
                    user.save()
                    send_single_mail(
                        "Account Register",
                        "Welcome to the Gharkharch app, hope you enjoy this app and hope it will help in your daily calculation\n here your activation code \n Code :"+str(otp),
                        email,
                        False
                    )
                    return JsonResponse(serializer.data,status = status.HTTP_202_ACCEPTED)
                else:
                    return JsonResponse({"response":"email already exits"},status = status.HTTP_226_IM_USED)
            except Exception as e:
                user.delete()
                return JsonResponse({'error':str(e)},status = status.HTTP_406_NOT_ACCEPTABLE)
        return JsonResponse(serializer.errors,status = status.HTTP_406_NOT_ACCEPTABLE)


@csrf_exempt
def validate_account(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = RegisterSerializer(data = data)
        if serializer.is_valid():
            try:
                email = serializer.data['email']
                otp = serializer.data['otp']
                if(UserModel.objects.filter(email=email).exists()):
                    user = UserModel.objects.get(email=email)
                    if (user.otp == otp):#check time less than 2 minutes
                        user.logged_in = True
                        user.save()
                        return JsonResponse({"response":"activate"},status = status.HTTP_202_ACCEPTED)
                    else:
                        return JsonResponse({"response":"otp not matches"},status = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
                else:
                    return JsonResponse(status = status.HTTP_404_NOT_FOUND)
            except Exception as e:
                 return JsonResponse({'error':str(e)},status = status.HTTP_406_NOT_ACCEPTABLE)
    return JsonResponse(serializer.errors, status = status.HTTP_406_NOT_ACCEPTABLE)

@csrf_exempt
def logout_account():
    pass
def deactivate_account():
    pass


