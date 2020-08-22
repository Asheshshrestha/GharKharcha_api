from django.urls import include,path
from api.accounts.views import UserListView,UserSignupView

urlpatterns = [
    #path('users/',include('users.urls')),
    path('rest-auth/',include('rest_auth.urls')),
    path('user-list/',UserListView.as_view(),name='user-list'),
    path('signup/',UserSignupView,name='signup')
]