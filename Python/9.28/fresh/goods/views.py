import random
import datetime

from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.paginator import InvalidPage
from django.http import Http404

from user.models import UserModel
from user.utils import login_required
from goods.models import CategoryModel,CategoryGoodsModel,GoodsModel,CommentModel
from cart.models import CartModel
from common.common import cart_count_goods

from haystack.views import SearchView
# Create your views here.



def index(request):
    """主页"""
    # 拿出所有的分类
    category_list = CategoryModel.objects.all()
    # 分别取出分类下的最新的商品
    new_goods_dict = {} # 存储每个分类下的最新的商品
    for category in category_list:
        # 直接通过商品分类id从goods中获取当前分类的商品
        goods_list = GoodsModel.objects.filter(category_id=category.id).order_by('-id')[:4]
        # 拿到所有的goods的id
        # goods_ids = [goods.goods_id for goods in goods_list]
        # goods_info_list = GoodsModel.objects.filter(id__in=goods_ids)
        new_goods_dict[category] = goods_list

    # 统计购物车中商品的数量
    cart_count = cart_count_goods(request,CartModel)

    context = {
        'new_goods_dict':new_goods_dict,
        'cart_count':cart_count
    }
    return render(request,'goods/index.html',context)

def list(request,category_id,sort,page_num):
    """商品列表视图"""
    """category_id: 分类的id
        page_num: 获取当前页的页码
        sort: 排序字段(默认: default,价格: price,人气: popular)"""
    category = CategoryModel.objects.get(id=category_id)
    # 取该类型最新的两个商品
    news = GoodsModel.objects.filter(category_id=category_id).order_by('-id')[:2]
    # 外键的用法
    # news = category.goodsmodel_set.order_by('-id')[:2]
    goods_list = []
    if sort == 'default': # 默认排序, 最新的在上面
        goods_list = GoodsModel.objects.filter(category_id=category_id).order_by('-id')
    elif sort == 'price': # 价格排序
        goods_list = GoodsModel.objects.filter(category_id=category_id).order_by('-price')
    elif sort == 'popular': # 按人气排序
        goods_list = GoodsModel.objects.filter(category_id=category_id).order_by('-popular')

    # 根据商品的列表goods_list 进行分页
    paginator = Paginator(goods_list,2)
    page = paginator.page(page_num)


    cart_count = cart_count_goods(request,CartModel)
    context = {
        'category':category, # 商品的分类对象
        'news':news,  # 新品推荐
        'goods_list':goods_list, # 排序后的商品列表
        'sort':sort,  # 排序的条件
        'cart_count':cart_count, # 购物车中的商品数量
        'page':page,
        'page_num':page_num  #当前的页数
    }
    return render(request,'goods/list.html',context)

def detail(request,goods_id):
    """某个商品详细信息,goods_id上具体的某个商品"""
    goods = GoodsModel.objects.get(id=goods_id)
    goods.popular += 1 # 增加商品的人气值
    goods.save()
    # news = GoodsModel.objects.filter(category_id=goods.category_id).order_by('-id')[:2]
    # 利用orm外键的特性
    news = goods.category.goodsmodel_set.order_by('-id')[:2]
    # 购物车内商品的数量
    cart_count = cart_count_goods(request,CartModel)

    # 记录最近的浏览记录, 在用户中心使用
    # 判断是否已经登陆
    if request.session.has_key('user_id'):
        user_id = request.session.get('user_id')
        goods_id_list = request.session.get(str(user_id),[])
        if not goods_id_list: # 判断是否有浏览记录
            goods_id_list.append(goods.id)
        else:
            # 如果已经存在浏览的商品, 删除掉这一个
            if goods_id in goods_id_list:
                goods_id_list.remove(goods_id)
            goods_id_list.insert(0,goods_id) # 添加元素到列表的第一个
            if len(goods_id_list) > 5: # 如果超过5个浏览记录, 删除最后一个
                del goods_id_list[-1]
        # 把最近浏览的商品存储在session中  以user_id的值为key
        request.session[user_id] = goods_id_list
    return render(request,'goods/detail.html',{'goods':goods,'news':news,'cart_count':cart_count})

class MySearchView(SearchView):
    """继承haystack的SearchView"""
    def build_page(self):
        """
        Paginates the results appropriately.

        In case someone does not want to use Django's built-in pagination, it
        should be a simple matter to override this method to do what they would
        like.
        """
        try:
            page_no = int(self.request.GET.get('page', 1))
        except (TypeError, ValueError):
            raise Http404("Not a valid number for page.")

        if page_no < 1:
            raise Http404("Pages should be 1 or greater.")

        start_offset = (page_no - 1) * self.results_per_page
        self.results[start_offset:start_offset + self.results_per_page]

        # 排序
        sort = self.request.GET.get('sort', 'id')
        paginator = Paginator(self.results.order_by('-'+sort), self.results_per_page)

        try:
            page = paginator.page(page_no)
        except InvalidPage:
            raise Http404("No such page!")

        return (paginator, page)
    def extra_context(self):
        """重写附加内容的函数"""
        # 获取所有的商品类别
        category_list = CategoryModel.objects.all()
        news = []  # 存储每个分类下2个最新商品
        for category in category_list:
            goods_list = GoodsModel.objects.filter(category_id=category.id).order_by('-id')[:2]
            news.extend(goods_list)

        # 统计购物车中商品的数量
        cart_count = cart_count_goods(self.request, CartModel)
        context = {
            'news': [random.choice(news),random.choice(news)],
            'cart_count': cart_count,
            'sort':self.request.GET.get('sort','id')
        }
        return context

def comment(request,goods_id):
    print(goods_id)
    context = []
    comment_list = CommentModel.objects.filter(goods_id=goods_id)
    for comment in comment_list:
        username = comment.user_id.username
        content = comment.content
        context.append({'username':username,'content':content})
    return JsonResponse({'context':context})

@login_required
def add_comment(request):
    user_id = request.session.get('user_id')
    goods_id = request.POST.get('goods_id')
    comment = CommentModel()
    comment.content = request.POST.get('content')
    comment.user_id = UserModel.objects.get(id=user_id)
    comment.goods_id = GoodsModel.objects.get(id=goods_id)
    comment.create_time = datetime.datetime.now()
    comment.vote_number = 0
    comment.save()
    return redirect('/goods/detail/{}/'.format(request.POST.get('goods_id')))

