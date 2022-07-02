from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import (TemplateView, CreateView,
                                  ListView, DeleteView,
                                  DetailView)
from django.http import HttpResponseRedirect
from .models import Posts, Comments
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

# Create your views here.


class Index(TemplateView):
    template_name = "post/index.html"


class PostCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('post:post_list')
    form_class = PostForm
    success_message = "Your Post is created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetails(DetailView):
    model = Posts
    template_name = 'post/post_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        post = get_object_or_404(Posts, slug=slug)
        if Posts.objects.all():
            all_posts = Posts.objects.all()
            popular = Posts.objects.order_by('-likes')[:5]

            liked = bool(post.likes.filter(id=self.request.user.id).exists())
            comments = Comments.objects.filter(post=post, parent=None)
            replies = Comments.objects.filter(post=post).exclude(parent=None)
            context['comments'] = comments
            context['popular_posts'] = popular
            context['post'] = post
            context['like_count'] = post.like_count()
            context['liked'] = liked

        return context


class Post(TemplateView):
    template_name = "post/index.html"


class PostList(ListView):
    context_object_name = 'post_list'
    # template_name = 'blog/blog_list.html'
    template_name = "post/post_list.html"
    queryset = Posts.objects.all()
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        popular = Posts.objects.order_by('-likes')[:5]
        context['popular_posts'] = popular
        return context


def LikeView(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post:post_details', args=[slug]))


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post:post_list')


def CommentView(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    user = request.user
    content = request.POST['comment']
    parent = None
    if 'parent_comment' in request.POST:
        parent = request.POST['parent_comment']
    comment = Comments.objects.create(
        post=post, user=user, content=content, parent=parent)
    comment.save()

    return HttpResponseRedirect(reverse('post:post_details', args=[slug]))
