from django.contrib import admin

# Register your models here.
from .models import Author,Article

# 设置哪些字段是可以显示的
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','age']
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','type','public_date','author']

admin.site.register(Author,AuthorAdmin)
admin.site.register(Article,ArticleAdmin)