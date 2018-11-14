from django.shortcuts import render,get_object_or_404
from  blog.models import  Post ,Comment
from taggit.models import Tag
from django.db.models import Count
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from .form import EmailPostForm,CommentFrom
from django.views.generic import  ListView

# Create your views here.
# FBV函数试图
#CBV 类视图
#minxins 可服用的类模块
# class PostListView(ListView):
    # queryset 是查询所有已发布的文章
    # 可以不用queryset 通过指定 model = post ，会进行 post.object.all 查询所有文章
    # model = Post
    # queryset = Post.published.all()
    # posts 设置为模板变量的名称 不过 不设置 默认的名称就是object——list
    # context_object_name = "posts"
    # paginate_by = 2
    # template_name = "blog/post/list.html"
    #返回分页的变量的名称 是page_obj


def post_list(request,tag_slug=None):
    posts=Post.published.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        posts=posts.filter(tags__in=[tag])



    # posts=Post.published.all()
    paginator=Paginator(posts,2)#每页两篇文章
    page=request.GET.get('page')
    try:
       posts= paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return  render(request,'blog/post/list.html',{"posts":posts,"page":page,"tag":tag})


def post_detail(request,year,month,day,slug):
    post=get_object_or_404(Post, slug=slug, status="publish", publish__year=year,publish__month=month, publish__day=day)
    # 列出文章的所有品论
    comments=post.commments.filter(active=True)
    new_comment = None
    if request.method=="POST":
        comments_form = CommentFrom(request.POST)
        if comments_form.is_valid():
            # 通过表单直接创建新的数据对象 ，但是不保存在数据库中
            new_comment=comments_form.save(commit=False)
    #         设置外键为当前对象
            new_comment.post=post
    #        最后将评论写入数据库
            new_comment.save()
    else:

        comments_form=CommentFrom()
    #     相近的tag的文章列表
    # flat=True 让结果变成一个列表
    # annotate聚合函数
    post_tag_ids=post.tags.values_list("id",flat=True)
    similar_tag=Post.published.filter(tags__in=post_tag_ids).exclude(id=post.id)
    # 使用count对每个文章按照标签计数，并且声称一个新的字段same_tags用于存放技术的结果
    similar_posta=similar_tag.annotate(same_tags=Count("tags")).order_by("-same_tags","-publish")[:2]

    return  render(request ,'blog/post/detail.html',{"post":post,
                                                     "comments":comments,
                                                     "new_comment":new_comment,
                                                     "comments_form":comments_form,
                                                     "similar_posta":similar_posta})

def post_share(request,post_id):
    #通过id 获取post对象
    post =get_object_or_404(Post,id=post_id,status="publish")
    send=False
    if request.method=="POST":
        # 表单被提交
        form =EmailPostForm(request.POST)

        # 如果返回false ，form errors
        if form .is_valid():
            # 验证表单数据
            cd=form.cleaned_data
             #发送邮件
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject="{} share reading ".format(cd["name"])
            message="reading comments{},文章链接{} ".format(cd["comment"],post_url)
            send_mail(subject,message,cd["email"],[cd["to"]])
            send = True
    else:
        # 创建一个很空白的form 对象 展示 在页面中一个空白 的表单供用户去填写
        form=EmailPostForm
    return  render(request,"blog/post/share.html",{'post':post,"form":form,"send":send})
