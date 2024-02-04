from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
    return HttpResponse("~Welcome sailor to the matrix. Its going to be rocking from here on~")
