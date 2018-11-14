from django.db import models
from  django.urls import  reverse
from  django.contrib.auth.models import User
from  django.utils import timezone
from taggit.managers import  TaggableManager
import  datetime
# from django.contrib import admin
# 数据架构 data schema
# scheam 是一个数据库名词，一般值的是数据库中的组织模式或者是架构
# Create your models here.
# post .objects.my_manager() 提供一个新的方法
#post.mymanager.all()
# 创建模型管理器
class PublishManager(models.Manager):
    def get_queryset(self):
        return  super(PublishManager,self).get_queryset().filter(status="publish")


class Post(models.Model):
        STATUS_CHOICES=(("draft","草稿"),("publish","发布"))
        title=models.CharField(max_length=200,verbose_name="标题")
        slug=models.SlugField(max_length=200,unique_for_date="publish")
        # RELATED_name 设置从user到post的反向关联关系 ，用blog_post位这个
        # 反响关连关系名名
        author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
        boby=models.TextField(verbose_name="文本内容")
        # timezone .now包含时区的时间对象
        publish=models.DateTimeField(default=timezone.now)
        # auto_now_add=True 表示当创建一行数据的时候，自动用创建数据的时间填充
        created=models.DateTimeField(auto_now_add=True)
        # auto_now=True每次根性时间的时候都会用当前时间填充
        update=models.DateTimeField(auto_now=True)
        status=models.CharField(max_length=10,choices=STATUS_CHOICES,default="draft")
        class Meta:
            db_table="blog"
            ordering=("-publish",)
        def __str__(self):
            return self.title
# @admin.register(Post)
# class blogeModels(admin.ModelAdmin):
#     list_display = ('title',)
        objects=models.Manager()# 默认的管理器
        published=PublishManager() #自定义的管理器
        tags=TaggableManager()#模型管理器


        # 创建超联接到具体的数据对象
        def get_absolute_url(self):
            return  reverse("blog:post_detail",args=[self.publish.year,
                                                     self.publish.month,
                                                     self.publish.day,
                                                     self.slug])


class Comment(models.Model):
    # 评论.post.comment_set
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="commments")
    name=models.CharField(max_length=80)
    email=models.EmailField()
    body=models.TextField()
    creater=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        db_table="comment"
        ordering=("creater",)
    def __str__(self):
        return self.name