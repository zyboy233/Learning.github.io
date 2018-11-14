from django.test import TestCase
import sys
# Create your tests here.

def gen(num):
    while num<10:
        yield num
        num += 1
for num in gen(5):
    print(num)

alist = [1,8,-3,4,-5]

list = sorted(alist,key=lambda x: abs(x),reverse=True)
print(list)

alist = [1,4,7,30]
blist = [3,5,87,7]

for a,b in zip(alist,blist):
    pass


