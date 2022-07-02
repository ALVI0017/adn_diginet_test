from django.forms import ModelForm, TextInput
from .models import Posts, Comments


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'description', 'image']


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['content']
