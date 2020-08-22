import json
from rest_framework import generics
from urllib import request 
from rest_framework import status
from rest_framework.response import Response
from api.accounts.models import User
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.accounts.serializers import (UserSerializer,
                                        LoginSerializer,
                                        SignupSerializer)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
def UserSignupView(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =SignupSerializer(data = data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            password1 = serializer.validated_data['password1']
            password2 = serializer.validated_data['password2']
            if password1 == password2:
                try:
                    if User.objects.filter(phone=phone):
                        return JsonResponse({'response':'Number is already used'},safe=False,status = status.HTTP_226_IM_USED)
                    user = User.objects.create_user(phone,password1)
                    user.save()
                except Exception as e:
                    return JsonResponse(str(e),safe=False)
                return JsonResponse({'phone':str(user)},safe=False,status = status.HTTP_201_CREATED)
            else:
                return JsonResponse({'response':'Password doesnot match'},safe=False,status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


def UserLoginView(request):
    pass
def UserLogoutView(request):
    pass
