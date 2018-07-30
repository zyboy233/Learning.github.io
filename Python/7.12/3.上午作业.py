

# 声明方法1
# 声明一个txt文件,里面存放1000条数据,每条数据长度为10,包含大小写字母和数字
#
# 声明方法2
# 读取txt文件里面所有的数据, 如果该条数据只有数字,那么创建一个txt文件保存起来
#
# 声明方法3
# 读取txt文件里面所有的数据, 如果该条数据只有字母,那么创建一个txt文件保存起来
#
# 声明方法4
# 读取txt文件里面所有的数据, 如果该条数据包含字母和数字,那么创建一个txt文件保存起来

import random
# 1.
def writeFun():
    f = open('test.txt','w',encoding='utf-8')
    str1 = ''
    for i in range(65,91):
        str1 += chr(i)
    for i in range(97,123):
        str1 +=chr(i)
    for i in range(10):
        str1 +=str(i)
    print(str1)
    for var in range(1000):
        ran_str = ''
        for i in range(10):
            ran_str += random.choice(str1)
        f.write(ran_str+'\n')
    f.close()
# 2.
def digitFun():
    with open('test.txt','r',encoding='utf-8') as f:
        lines = f.readlines()
        with open('testDigit.txt','w',encoding='utf-8') as f1:
            for line in lines:
                if line[:10].isdigit():
                    f1.write(line)
        f1.close()
    f.close()

# 3.
def alphFun():
    with open('test.txt','r',encoding='utf-8') as f:
        lines = f.readlines()
        with open('testAlph.txt','w',encoding='utf-8') as f1:
            # 1.
            # for line in lines:
            #     if line[:10].isalpha():
            #         f1.write(line)
            # 2.
            # for line in lines:
            #     count = 0
            #     for char in line:
            #         if (ord(char) >= 65 and ord(char) <=90) or (ord(char) >=97 and ord(char)<=122):
            #             count += 1
            #     if count == 10:
            #         f1.write(line)
            # 3.
            for line in lines:
                isAllAlph = True
                for var in line[0:10]:
                    if var.isdigit():
                        isAllAlph = False
                        break
                if isAllAlph == True:
                    f1.write(line)
        f1.close()
    f.close()

# 4.
def digitAlphFun():
    with open('test.txt','r',encoding='utf-8')as f:
        lines = f.readlines()
        with open('testDigitAlph.txt','w',encoding='utf-8')as f1:
            for line in lines:
                if not (line[:10].isalpha() or line[:10].isdigit()):
                    f1.write(line)
        f1.close()
    f1.close()

# writeFun()
# digitFun()
# alphFun()
# digitAlphFun()