from django.template import Library

register = Library()
@register.filter
def toList(value):
    num_list = list(range(1,value+1))
    return num_list

@register.filter
def listLen(value):
    num = len(value)
    return num
@register.filter
def toUrl(L):
    index = L[0]
    json = L[1]
    url = json['data'][index]['url']
    return url