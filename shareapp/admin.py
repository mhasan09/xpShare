from django.contrib import admin

# Register your models here.
from .models import Author,Category,Article, Comment

class AuthorModel(admin.ModelAdmin):

    list_display = ["__str__"]
    search_fields = ["__str__", "details"]
    class Meta:
        model = Author
admin.site.register(Author , AuthorModel)

class ArticleModel(admin.ModelAdmin):

    list_display = ["__str__", "posted_on"]
    search_fields = ["__str__", "details"]
    list_filter = ["posted_on", "category"]
    list_per_page = 10
    class Meta:
        model = Article

admin.site.register(Article, ArticleModel)


class CategoryModel(admin.ModelAdmin):

    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        model = Category
admin.site.register(Category, CategoryModel)

class CommentModel(admin.ModelAdmin):

    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        model = Comment
admin.site.register(Comment, CommentModel)


