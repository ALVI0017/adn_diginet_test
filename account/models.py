from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(blank=True, max_length=20)
#     address = models.CharField(blank=True, max_length=200)
#     city = models.CharField(blank=True, max_length=200)
#     district = models.CharField(blank=True, max_length=200)
#     zip = models.CharField(blank=True, max_length=200)
#     country = models.CharField(blank=True, max_length=200)
#     image = models.ImageField(blank=True, upload_to='user_img')

#     def __str__(self):
#         return self.user.username

#     def user_name(self):
#         return f'{self.user.first_name} {self.user.last_name}[{self.user.username}]'

#     def image_tag(self):
#         return mark_safe(f'<img src="{self.image.url}" heights="50" width="50" />')
#     image_tag.short_description = 'Image'

#     def imageUrl(self):
#         return self.image.url if self.image else ""
