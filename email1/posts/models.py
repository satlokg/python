from django.db import models
from django import forms
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    objects = models.Manager

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content']