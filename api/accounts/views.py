from django.shortcuts import render
from api.accounts.serializers import EmailInputSerializer,RegisterSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from library.otp_generator import generateOTP
from api.accounts.models import UserModel
from rest_framework import status
# Create your views here.


@csrf_exempt
def register_request(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmailInputSerializer(data = data)
        if serializer.is_valid():
            try:
                email = serializer.data['email']
                if(not UserModel.objects.filter(email=email).exists()):
                    otp = generateOTP()
                    user = UserModel(email=email,otp=otp)
                    user.save()
                    """
                    send otp through mail
                    """
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
                    print("ashesh")
                    print(user.email)
                    if (user.otp == otp):
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


