from django.template import Library

register = Library()

@register.filter
def total_price(num,price):
    return num * price
