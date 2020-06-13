
from django.shortcuts import render, reverse, HttpResponseRedirect
from files.models import File

# Create your views here.


def home(request):
    files = File.objects.all()
    return render(request, 'home.html', {'files': files})
