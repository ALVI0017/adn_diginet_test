from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class Index(TemplateView):
    template_name = "post/index.html"


class Post(TemplateView):
    template_name = "post/index.html"
