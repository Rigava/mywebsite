from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [ 
    {'author': 'arun',
     'title': 'Blog post 1',
     'content': 'first post',
     'date_posted': 'Jan 1 2024'
    },
    {'author': 'om',
     'title': 'Blog post 2',
     'content': 'second post',
     'date_posted': 'Feb 1 2024'
    }
]
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'main.html',context)