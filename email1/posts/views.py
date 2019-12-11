from django.shortcuts import render,redirect
from posts.models import Posts, PostsForm, Category
# Create your views here.


def index(request):
    form = PostsForm()
    data = Posts.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    return render(request, 'index.html', {'title': 'Add New Post', 'form': form, 'rows': data, 'categories': categories})
