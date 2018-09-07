from django.template import Library

register = Library()

@register.filter()
def addcontent(value):
    if value['has_kuang']== True:
        return '有'
    else:
        return '没有'