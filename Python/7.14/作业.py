
# 作业：在控制台输入信息，程序执行不同命令：
# 控制台输入1：添加学生信息，学生所有信息需要通过控制台输入
# 控制台输入2：修改学生信息，需要在控制台指明哪个学生的信息需要修改，
#   同时在控制台输入修改的内容
# 控制台输入3：删除学生信息，需要在控制台指明哪个学生需要被删除
# 控制台输入4：查询所有学生信息
# 控制台输入其他数字：退出查询系统

import sqlite3

"""
con = sqlite3.connect('stuInfoDB')
cursor = con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS stuInfo(stuId text,stuName text,stuSex text CHECK(stuSex IN ("男","女")),age text)')
stuDict = {'学号':'','姓名':'','性别':'','年龄':''}
stuDictToTable = {'学号':'stuId','姓名':'stuName','性别':'stuSex','年龄':'age'}
print(stuDict)
while True:
    order = int(input('请输入你的指令:'))
    if order == 1:
        print('添加学生信息:')
        for k in stuDict.keys():
            stuDict[k] = input('输入学生{}:'.format(k))
        con.execute('INSERT INTO stuInfo VALUES ("{}","{}","{}","{}")'.format(stuDict['学号'],stuDict['姓名'],stuDict['性别'],stuDict['年龄']))
        con.commit()
    if order ==2:
        print('修改学生信息:')
        stuName = input('请输入学生姓名:')
        cursor.execute('SELECT * FROM stuInfo WHERE stuName = "{}"'.format(stuName))
        stuInfo = cursor.fetchone()
        tagsForChange = input('输入修改的项:')
        for i in list(tagsForChange.split(',')):
            tag = input('{}:'.format(i))
            cursor.execute('UPDATE stuInfo SET "{}"="{}" WHERE stuName = "{}"'.format(stuDictToTable[i],tag,stuName))
            con.commit()
    if order == 3:
        print('删除学生信息:')
        stuName = input('请输入学生姓名:')
        cursor.execute('DELETE FROM stuInfo WHERE stuName = "{}"'.format(stuDictToTable[stuName]))
        print('删除成功')
    if order == 4:
        print('所有学生信息:')
        cursor.execute('SELECT * from stuInfo')
        allStu = cursor.fetchall()
        print(allStu)
    else:
        break
"""

# 甲乙丙三人玩找七游戏，从甲开始，甲说任意一个数，乙在此基础上加1，丙加2，依次类推，
# 如果如果谁轮到了7的倍数或者包含7的数字，那么这个人需要将这个数字
# 保存起来，一直到100结束，最后统计每个人分别保存的数字的总和。
import  random
class Person(object):
    def judge(self,num = ''):
        if num%7==0 or '7' in str(num):
            return True
p1 = p2 = p3 =Person()
p1List = []
p2List = []
p3List = []
num = random.randint(1,100)
print(num)
while num<100:
    num +=1
    if p2.judge(num):
        p2List.append(num)
    num += 1
    if p3.judge(num):
        p3List.append(num)
    num += 1
    if p1.judge(num):
        p1List.append(num)
print(p1List,p2List,p3List)
print(sum(p1List),sum(p2List),sum(p3List))



