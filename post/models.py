
# Create your models here.
from datetime import datetime
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django_quill.fields import QuillField
from django.utils.text import slugify
import random
n = random.randint(0, 12312313123)


class Posts(models.Model):

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ["-created_at"]
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, max_length=200, unique=True)
    description = QuillField()
    image = models.ImageField(
        blank=True, default='avatar.jpg', upload_to='blog_img')
    likes = models.ManyToManyField(
        User, related_name='blog_post', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.title}'

    def imageUrl(self):
        return self.image.url if self.image else ""

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # uniqueness
        self.slug = self.slug+str(n)
        super(Posts, self).save(*args, **kwargs)


class Comments(models.Model):
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    parent = models.IntegerField(null=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)
    post = models.ForeignKey(Posts,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True,
                             related_name='post_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.title} {self.user.username}'

    def get_date(self):
        time = datetime.now()
        if self.created_at.day == time.day:
            return f"{str(time.hour - self.created_at.hour)} hours ago"
        if self.created_at.month == time.month:
            return f"{str(time.day - self.created_at.day)} days ago"
        if self.created_at.year == time.year:
            return f"{str(time.month - self.created_at.month)} months ago"
        return self.created_at
