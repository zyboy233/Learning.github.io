from django.contrib import admin
from  .models import  Post
from .models import Comment
# Register your models here.
@admin.register(Post)
class postmodels(admin.ModelAdmin):
    list_display = ("title","slug")
    list_filter = ("status",)
    search_fields = ("title",)
    # raw_id_fields = ("author",)
@admin.register(Comment)
class CommmentModels(admin.ModelAdmin):
    list_display = ("name","post","body","email","active",)
    list_filter = ('active',"creater","update")
    search_fields = ("name","email","body")