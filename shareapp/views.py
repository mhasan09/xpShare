from django.shortcuts import render,get_object_or_404,redirect
from .models import Article,Author,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from .form import createArticle, createRegisterUser, createAuthor
from django.contrib import messages


# Create your views here.
def getIndex(request):
    post = Article.objects.all()

    search = request.GET.get('q')
    if search:
        post = post.filter(
            Q(title__icontains=search)|
            Q(body__icontains=search)
        )
    paginator = Paginator(post, 8)  # Show 25 contacts per page

    page = request.GET.get('page')
    total_article = paginator.get_page(page)
    context = {
        "post" : total_article
    }
    return render(request, "index.html", context)

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

def getTopic(request, name):
    cat = get_object_or_404(Category,name=name)
    post = Article.objects.filter(category= cat.id)
    paginator = Paginator(post, 8)  # Show 25 contacts per page

    page = request.GET.get('page')
    total_article = paginator.get_page(page)
    return render(request, "category.html" , {"post":total_article , "cat" : cat},)

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
            else:
                messages.add_message(request,messages.ERROR,"Username or Password mismatch")
                return render(request, "login.html")
    return render(request, "login.html")

def getLogout(request):
    logout(request)
    return redirect('index')

def getCreate(request):
   if request.user.is_authenticated:
       u=get_object_or_404(Author,name=request.user.id)
       form = createArticle(request.POST or None, request.FILES or None)
       if form.is_valid():

           instance = form.save(commit=False)
           instance.article_author = u
           instance.save()
           return redirect('index')

       return render(request, 'create.html', {'form': form})
   else:
       return redirect('login')

def getSeperateProfile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User,id=request.user.id)
        author_profile=Author.objects.filter(name=user.id)
        if author_profile:
            author_user = get_object_or_404(Author,name = request.user.id)
            post = Article.objects.filter(article_author=author_user.id)
            return render(request, 'logged_in_profile.html', {"post": post, "user": author_user})
        else:
            form = createAuthor(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.name = user
                instance.save()
                return redirect('profile')
            return render(request, 'createAuthor.html', {"form": form})
    else:
        return redirect('login')

def getUpdate(request,id):
   if request.user.is_authenticated:
       u=get_object_or_404(Author,name=request.user.id)
       post = get_object_or_404(Article,id=id)
       form = createArticle(request.POST or None, request.FILES or None, instance= post)
       if form.is_valid():

           instance = form.save(commit=False)
           instance.article_author = u
           instance.save()
           messages.add_message(request, messages.SUCCESS, "Post has been updated")
           return redirect('profile')

       return render(request, 'create.html', {'form': form})
   else:
       return redirect('login')

def getDelete(request ,id):
   if request.user.is_authenticated:
       post = get_object_or_404(Article,id=id)
       post.delete()
       messages.add_message(request, messages.WARNING, "Post has been Deleted")
       return redirect('profile')

   else:
       return redirect('login')

def getRegister(request):
    form = createRegisterUser(request.POST or None)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.save()
        messages.SUCCESS(request,"Registration Successfully Completed")
        return redirect('login')
    return render(request,'register.html',{"form" : form})