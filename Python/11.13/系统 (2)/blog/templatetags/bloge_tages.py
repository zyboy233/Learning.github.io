from django import  template
# from django.template import  Library
from blog.models import Post
from django.db.models import Count
# 用来注册一个自定义的标签
register=template.Library()
# 注册文章总数
@register.simple_tag
def total_posta():
     return Post.published.count()
@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts():
     latest_posts=Post.published.order_by("-publish")
     return  {"latest_posts":latest_posts}
@register.simple_tag
def get_most_commment_posts():
     return  Post.published.annotate(total_commments=Count('commments')).order_by("-total_commments")[:2]

@register.filter
def post_add(num,count):
     return  num+count

@register.filter
def myCut(value):  # 把传递过来的参数arg替换为'~'
    return value.replace(value,"!")
