from django.contrib import admin
from posts.models import Posts as Post, Category

# Register your models here.
admin.site.register([Post, Category])
