from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError
from django.contrib.auth.models import User
# Create your models here.


def min_length_check(val):
        if len(val) <= 10:
             raise validators.ValidationError(
                 "%(val)s Must Greater than 10", params={'val': val})


class Category(models.Model):
    title = models.CharField(
        validators=[
            min_length_check
        ],
        max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return self.title

class Posts(models.Model):
    title = models.CharField(
        validators=[
            min_length_check
            ],
        max_length=255)
    content = models.TextField(
        validators=[
        min_length_check
    ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    objects = models.Manager
    def __str__(self):
        return self.title

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'user']
    def clean(self):
        fields = self.cleaned_data
        keys = list(fields.keys())
        if(len(fields['title']) <= 10):
           raise validators.ValidationError("%(val)s Must Greater than 10", params={'val':keys[0]})
        if(len(fields['content']) <= 10):
           raise validators.ValidationError(
               "%(val)s Must Greater than 10", params={'val': keys[1]})
