from django.urls import path
from . import views
from .views import *
from blog_post import settings

app_name = "post"

urlpatterns = [
    path("", views.Index.as_view(), name="home"),
    path("list/", PostList.as_view(), name="post_list"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("details/<slug:slug>/", PostDetails.as_view(),
         {'document_root': settings.MEDIA_URL}, name="post_details"),
    path("like/<slug:slug>", LikeView, name='like_post'),
    path("<slug:slug>/comment/", CommentView, name='post_comment'),
    path('<slug:slug>/delete/', PostDelete.as_view(), name="delete_post"),


    # path("about/", views.AboutUs, name="about"),

]
