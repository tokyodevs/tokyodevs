from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_variable = ''
    context = {"context_variable": context_variable}
    return render(request,'index.html', context)


def index3(request):
    return render(request,'index.html')


def index1(request):
    return HttpResponse("Hello, World!")




