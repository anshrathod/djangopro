from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView
from .models import User

def main(request):
    template = loader.get_template('example/main.html')
    return HttpResponse(template.render({}, request))

def index(request):
    model = User
    fields = ['first_name', 'last_name', 'email', 'username', 'password']
    template = loader.get_template('example/index.html')
    return HttpResponse(template.render({}, request))

def contact(request):
    template = loader.get_template('example/contact.html')
    return HttpResponse(template.render({}, request))

def about(request):
    template = loader.get_template('example/about.html')
    return HttpResponse(template.render({}, request))

def gallery(request):
    template = loader.get_template('example/gallery.html')
    return HttpResponse(template.render({}, request))

class AccCreate(CreateView):
    model = User
    fields = ['first_name','last_name','email','username','password']