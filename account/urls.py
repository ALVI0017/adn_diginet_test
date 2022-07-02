from django.urls import path
from . import views
from .views import *

app_name = "account"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="sign_up"),
    path("signin/", SignIn.as_view(), name="sign_in"),
    path('logout/', LogoutView.as_view(), name="logout")
]
