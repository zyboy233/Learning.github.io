

import re


pattern = re.compile('(\d+)(\w+)')
content = '1321efsef4554'
result = pattern.match(content)
print(result)

content = '32545646513215'
pattern = re.compile('.*?(5.*?5)')
result = pattern.match(content)
print(result)

print('---------------------')

content = '  I love you I'
pattern = re.compile('I')
result = pattern.sub('hahah',content)
print(result)
