from django.shortcuts import render
from api.accounts.serializers import EmailInputSerializer
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
                    return JsonResponse(serializer.data,status = status.HTTP_202_ACCEPTED)
                else:
                    return JsonResponse({"response":"email already exits"},status = status.HTTP_226_IM_USED)
            except Exception as e:
                user.delete()
                return JsonResponse({'error':str(e)},status = status.HTTP_406_NOT_ACCEPTABLE)
        return JsonResponse(serializer.errors,status = status.HTTP_406_NOT_ACCEPTABLE)
