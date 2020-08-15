from django.urls import path
from api.accounts.views import register_request,validate_account

urlpatterns = [
    path("register",register_request),
    path("activate",validate_account)
]
