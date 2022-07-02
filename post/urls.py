from django.urls import path
from . import views
from .views import *

app_name = "post"

urlpatterns = [
    path("", views.Index.as_view(), name="home"),
    # path("about/", views.AboutUs, name="about"),

]
