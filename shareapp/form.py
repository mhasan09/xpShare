from django import forms
from .models import Article
class createArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'article_author',
            'title',
            'body',
            'category',
            'image'
        ]