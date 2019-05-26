from django.shortcuts import render,get_object_or_404,redirect
from .models import Article,Author,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def getIndex(requests):
    post = Article.objects.all()
    context = {
        "post" : post
    }
    return render(requests, "index.html", context)

def getProfile(request,name):
    post_author = get_object_or_404(User,username=name)
    auth = get_object_or_404(Author, name=post_author.id)
    post = Article.objects.filter(article_author=auth.id)
    context = {
        "auth": auth,
        "post": post
    }
    return render(request, "profile.html",context)

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

def getLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')
    return render(request, "login.html")

def getLogout(request):
    logout(request)
    return redirect('index')