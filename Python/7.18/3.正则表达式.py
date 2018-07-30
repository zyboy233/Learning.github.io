import re
# 正则表达式
# 正则表达式可以判断目标字符串是否符合
# 特定的要求,比如判断是否为手机号,身份证号,邮箱号

"""
# digit
\d : 表示任意的一位数字
\d\d : 表示任意的两位数字
# world
\w : 表示任意的一个字母和数字
# space
\s : 表示空格

. : 表示任意的内容 1,2,3 a,b,c!@#
a. : 在a后面匹配任意的内容 ab  a1
* : 表示内容出现0次到多次
a.* : a a1 ab aaaa a11111
+ : 表示内容出现1次到多次
a.+ : aa ab a1 ac ad
? :表示内容出现0次到1次
a.?  : a a1 aaa
^ : 脱字符 表示以...开头
$ : 美元符 表示以...结尾

{n} : 表示内容重复n次
\d\d\d
\d{3}
{n,m} : 标志最少重复n次,最多重复5次
\d{3,5}
{n,} : 表示最少重复n次
{,m} : 表示最多重复m次
"""
# pettern 模式
# compile 编译
# 后面写正则表达式的内容
# ()代表从目标字符串当中获取的字符串的子串
# 每一个括号就是一个group组
pattern = re.compile('(\d+)(\w+)')
content = '123helloWorld'
result = re.match(pattern,content)
if result:
    # 返回的是一个匹配的对象
    print(result)
    # 返回的是符合要求的全部内容
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))
else:
    print('不符合')

pattern = re.compile('my')
result = re.match(pattern,'myself')
print(result.group(0))
# match匹配的是内容的开始部分
# 作用等同于 startwith
result = re.match(pattern,'love myself')
print(result)

pattern = re.compile('lalala')
result = re.match(pattern,' lalalaha')
print(result)

pattern = re.compile('my')
result = pattern.match('myself')
print(result)

# 贪婪模式与非贪婪模式
# 正则表达式默认为贪婪模式 尽量找到所有的符合要求的内容
# .* 称为贪婪模式
content = 'aabbababa11b22'
pattern = re.compile('(a.*b)')
result = pattern.match(content)
print(result)

# .*? 称为非贪婪模式
# 从a开始往后任意字符出现0次或多次知道遇见一个b 就结束
pattern = re.compile('(a.*?b)')
result = pattern.match(content)
print(result)

# 匹配任意字符开头
# 后面找到一个以b开头以b结尾的内容
pattern = re.compile('.*?(b.*?b)')
result = pattern.match(content)
print(result)

# * + 同为贪婪模式
# * 至少0次,至多无限次
# + 至少一次,至多无限次
pattern = re.compile('(a.+b)')
result  = pattern.match(content)
print(result)


print('hello \n world')
# raw string  会将字符串里面的字符输出出来
print(r'hello \n world')

title = '0123Hello World'
pattern = re.compile(r'\d\d\d')
# 匹配连续三个数字
pattern = re.compile(r'\d{3}')
result = pattern.match(title)
print(result)

# 匹配全国固话 0371-12345678

pattern = re.compile(r'(\d{4})-(\d{8})')
result = pattern.match('0371-87654321')
print(result)
print(result.group(1))
print(result.group(2))
# | 或者 设置用于不同情况的正则
pattern = re.compile('((haha|heihei)balabala)')
result = pattern.match('hahahalabala')
result = pattern.match('heiheibalabala')
print(result)

# 找到字符串当中第一个符合正则的内容
# 注意: 只找到第一个
pattern = re.compile(r'http')
# search
result = pattern.search('www.jd.com,http://www.taobao.com')
print(result)

pattern = re.compile(r'you')
result = pattern.search('I love you , I miss you , I hate you')
print(result)

pattern = re.compile(r'I')
result = pattern.search(' love you I')
print(result)

# findall 找到所有符合的内容
content = '12345,上山打老虎,老虎没打着,打只小松鼠,55555'
pattern = re.compile(r'\d{5}')
result = pattern.findall(content)
print(result)

# sub :替换子串(字符串的一部分)
# \s : 匹配空白部分
content = '杨过对战金轮法王,郭靖观战'
pattern = re.compile(r'杨\s*过')
result = pattern.sub('吕布',content)
print(result)
pattern = re.compile(r'金轮法王')
result = pattern.sub('服部半藏',result)
print(result)

key_word = [
    (r'杨\s*过','吕布'),
    (r'金轮法王','服部半藏'),
    (r'郭靖','东方不败')
]
print('----------------------------')
for pattern,replace in key_word:
    pattern = re.compile(pattern)
    content = pattern.sub(replace,content)
    print(content)

# 匹配手机号
# 13    147  15  x4  180 185-9

pattern = re.compile(r'^((13[0-9])|(14[7])|(15[0-3])|(15[5-9])|(18[0|5-9]))\d{8}$')
result = pattern.match('18003871820')
print(result)