import requests
from xml import etree
response = requests.get(url='https://www.shixiseng.com/interns?k=python&p=1')

print(response.text)
