from django.template import Library

register = Library()

@register.filter
def find_city(value):
    city = value['results'][0]['currentCity']
    return city
@register.filter
def find_date(value):
    # results.0.weather_data.0.date
    date = value['results'][0]['weather_data'][0]['date']
    return date
@register.filter
def find_temperature(value):
    temperature = value['results'][0]['weather_data'][0]['temperature']
    return temperature