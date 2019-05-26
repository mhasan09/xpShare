from django.shortcuts import render,get_object_or_404
from .models import Article,Author,Category
# Create your views here.
def getIndex(requests):
    post = Article.objects.all()
    context = {
        "post" : post
    }
    return render(requests, "index.html", context)

def getProfile(requests,name):
    return render(requests, "profile.html")

def getSingle(requests, id):
    post = get_object_or_404(Article, pk=id)
    first = Article.objects.first()
    last = Article.objects.last()
    related = Article.objects.filter(category=post.category).exclude(id=id)[:4]
    context = {
        "post" : post,
        "first" : first,
        "last" : last,
        "related" : related
    }
    return render(requests, "single.html", context)

def getTopic(requests, name):
    cat = get_object_or_404(Category,name=name)
    post = Article.objects.filter(category= cat.id)
    return render(requests, "category.html" , {"post":post , "cat" : cat},)