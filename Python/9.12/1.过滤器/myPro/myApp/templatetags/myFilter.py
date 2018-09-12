from django.template import Library

register = Library()

# 过滤器后面写过滤器的名字
# 如果名字不写 默认为函数名字
@register.filter
def add(value):

    return value + '----------------'
# 注册过滤器
@register.filter
def change_length(value):
    if len(value) > 10:
        return value[:10] + '...'
    return value
# 注册标签---------------------
@register.simple_tag
def myTag(value1,value2):
    if value1 == 'a':
        return '<a href="https://www.baidu.com">雄霸</a>'
    if value2 == 'b':
        return '<h1>天下</h1>'

import datetime
@register.simple_tag
def get_current_time():
    time = datetime.datetime.now()
    time = time.strftime('%Y-%m-%d %H:%M:%S')
    return '<h1>{}</h1>'.format(time)