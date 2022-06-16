#from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from . models import blogpost
def index(request):
    mypost = blogpost.objects.all()
    return render(request, 'blog/index.html', {'mypost': mypost} )
# Create your views here.
def blogposts(request, id):
    post = blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',{'post':post})