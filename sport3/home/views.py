from django.shortcuts import render, get_object_or_404
from news.models import MyNewsFb
# Create your views here.

def homeview(request):
    posts = MyNewsFb.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context=context)

def postdetail(request, id):
    post = get_object_or_404(MyNewsFb, pk=id)
    context = {
        'post': post,
    }
    return render(request, 'detailpost.html', context=context)