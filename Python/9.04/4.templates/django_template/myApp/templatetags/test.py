from django.template import Library
# 注册当前的数据 注册完以后重启pycharm  否则可能会崩溃
register = Library()
@register.filter
def add(value):
    pass
@register.filter
def girl_des(value):
    has = '没有'
    if value['hasKuang'] == True:
        has = '有'
    return '我的女朋友叫做' + value['name'] + ',身高' + value['height'] + 'cm,家里面' + has + '矿'