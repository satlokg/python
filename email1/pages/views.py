from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'index.html', {'title':'Home Page Title'})


def about(request):
    return render(request, 'about.html', {'title': 'About Page Title'})


def contact(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        zipcode = request.POST['zip']
        return render(request, 'contact.html', {'title': 'Contact Page Title','email':email, 'address':address, 'city':city, 'zipcode':zipcode})
    return render(request, 'contact.html', {'title': 'Contact Page Title'})


def member(request, cat_id, mem_id):
    return HttpResponse("<h1>Team Member ID : {} category ID: {}".format(mem_id, cat_id))


def team(request):
    if(request.method == "GET" and 'cat_id' in request.GET and 'mem_id' in request.GET):
        return HttpResponse("<h1>Team Member ID : {} category ID: {}".format(request.GET.get('mem_id'), request.GET.get('cat_id')))
    else:
        return HttpResponse("<h1>Team Members List </h1>")
