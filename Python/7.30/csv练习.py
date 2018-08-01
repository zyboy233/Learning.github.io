import csv

list1 = [['张三','李四'],['王五','陈六']]

with open('练习1.csv','w',newline='')as csv_file:
    writer = csv.writer(csv_file)
    for item in list1:
        writer.writerow(item)
    csv_file.close()
with open('练习1.csv','r',newline='')as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

def csv_list():
    tag = "Y"
    while tag== "Y":
        list = []
        columns = int(input('请输入列数:'))
        list.append([input('请输入第{}列:'.format(col+1))for col in range(columns)])
        with open('练习2.csv','a',newline='')as csv_file:
            writer = csv.writer(csv_file)
            for row in list:
                writer.writerow(row)
            csv_file.close()
        tag = input('是否继续输入? Y/N')
        if tag != "Y":
            break

dic = [{'name':'zhangsan','age':25},{'name':'lisi','age':20}]
list = []

with open('练习3.csv','w',newline='')as csv_file:
    for key in dic[0].keys():
        list.append(key)
    writer = csv.DictWriter(csv_file,fieldnames=list)
    writer.writeheader()
    for data in dic:
        writer.writerow(data)
with open('练习3.csv','r')as csv_file:
    reader = csv.DictReader(csv_file)
    for item in reader:
        print(item)
