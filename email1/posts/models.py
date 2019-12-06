from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError
# Create your models here.


class Posts(models.Model):
    def min_length_check(val):
        if len(val) <= 10:
            raise  validators.ValidationError("Value must be greater than 10")

    title = models.CharField(
        validators=[
            validators.validate_email,
            min_length_check
            ],
        max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    objects = models.Manager

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content']
