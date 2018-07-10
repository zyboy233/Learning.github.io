## python常见错误

1. SyntaxError: 'return' outside function
```javascript
while True:
    count += 1
    if count ==20:
        return
  ```
 >语法错误:return 不能在方法以外执行
 >>解决:将return放进方法体中
 
2. IndentationError: expected an indented block
```javascript
if count == 0:
print(count)
else:
  print('nothing')
```
>缩进错误:未正确缩进
>>解决:正确缩进

3. IndexError: string index out of range
```javascript
content = 'hello'
print(content[10])
```
>索引错误:字符串超出范围
>>解决:查看字符串长度,索引要小于字符串长度

4.ValueError: substring not found
```javascript
content = 'Hello World'
result = content.index('z')
print(result)
```
>值错误:子字符串未找到
>>解决:

5.AttributeError: 'tuple' object has no attribute 'remove'
```javascript
tp1 = ((),[],{},1,2,3,'a','b','c',3.14,True)
print(tp1)
```
>attribute 属性 object 对象
>>属性错误

6.KeyError: 'fond'
```javascript
dict1 = {
    'name':'张三',
    'age':17,
    'friend':['李四','王五','赵六','冯七']
}
print(dict1['fond'])
```
>key错误 没有指定的键值'fond'

7.TypeError: pop expected at least 1 arguments, got 0
```javascript
dict1 = {'a':1,'b':2}
dict1.pop()
```
>arguments 参数  expected 期望 at least 至少
>>类型错误:pop方法希望得到至少一个参数 但现在参数为0

8.SyntaxError: invalid syntax
```javascript
if True
    print(1)
```
>语法错误
>>解决:True后面加上:
