
import re

content = """
today is hot , I
want sleep, I
want go home
"""

pattern  = re.compile(r'.*?I(.*?)sleep')
result = pattern.search(content)
print(result)
# re.S忽略换行符
pattern = re.compile(r'.*? I(.*?)sleep',re.S)
result = pattern.search(content)
print(result)