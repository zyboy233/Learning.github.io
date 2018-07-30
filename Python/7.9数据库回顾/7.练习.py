# 1.计算0到100之和
# 2.计算n的n次方
# 3.鸡兔同笼,笼子里一共有32个头,96条腿,问各有几只?
# 4.有100只马,100担货物,大马一直可以驮3担,中马可以驮2担,
#     两只小马驮1担,问各有几只马?

# 1.
sum = 0
for i in range(101):
    sum += i
print('1+...+100=%s' % sum)

# 2.
n = 0
if n == 0:
    print(n)
else:
    mul = 1
    for i in range(n):
        mul = mul * n
    print(mul)
# n = 3
# str_sum = ''
# fuhao = '*'
# for i in range(1,n+1):
#     str_sum += str(n)
# str_sum = fuhao.join(str_sum)
# result = eval(str_sum)
# print(result)

# 3.
x = ''
y = ''
# x + y = 36
# 2x + 4y = 92 /// x + 2y =46
for  i in range(33):
    if i*2 + (32-i)*4 == 96:
        print('鸡:%s,兔:%s' % (i,32-i))

# 4.
for i in range(33):
    for j in range(100-i):
        if i*2+j*3+(100-i-j)/2 ==100:
            print('大马:%s,中马:%s,小马:%s' % (j,i,100-i-j))

enu = enumerate(range(20,30))
print(list(enu))



