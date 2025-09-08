from django.contrib import admin
from .models import Article, Comment

class CommetnInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommetnInline,
    ]

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "body",
        "author",
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

# Register your models here.
