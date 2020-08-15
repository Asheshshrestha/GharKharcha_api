from django.urls import path
from api.accounts.views import register_request

urlpatterns = [
    path("register",register_request)
]
