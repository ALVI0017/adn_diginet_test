from collections import UserList
from django.urls import path
from . import views
from .views import *

app_name = "account"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="sign_up"),
    path("signin/", SignIn.as_view(), name="sign_in"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('user/list/', UserList.as_view(), name="user_list"),
    path('user/<pk>/delete', UserDelete.as_view(), name="user_delete")
]
