from django.urls import path
from user.views import register,register_post,login,info,logout,all_order,address,upload
# 命名空间名称
app_name = 'user'

urlpatterns = [
    path('register/',register,name = 'register'),
    path('register_post/',register_post,name='register_post'),
    # 登陆接口
    path('login/',login,name='login'),
    # 个人中心
    path('info/',info,name='info'),
    # 退出登陆
    path('logout/',logout,name='logout'),
    # 全部订单
    path('all_order/<int:page_num>/',all_order,name = 'all_order'),
    # 收货地址
    path('address/',address,name = 'address'),
    # 文件上传
    path('upload/',upload,name = 'upload')
]