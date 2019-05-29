from django import forms
from .models import Article,Author
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class createArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = [

            'title',
            'body',
            'category',
            'image'
        ]

class createRegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'password1',
            'password2',
            'email',
            'username',

        ]

class createAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['profile_picture' , 'details']