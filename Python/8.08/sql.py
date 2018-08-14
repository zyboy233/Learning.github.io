#
# pymysql内置sql函数 与mySQL相连
# pymysql是与python3相匹配的nysql工具
# 在python2里面 需要使用MySQLdb 2009
import pymysql
# 在写这句代码的时候 要确保SQL里面已经创建了一个数据库 有表 有字段
db = pymysql.connect(host='localhost',user='root',password='123456',db='pythonDB',port=3306) # localhost
cursor = db.cursor()

# 增
# sql = 'insert into pythonTable(age,name,fond) VALUES (15,"zhaoliu","play")'
# cursor.execute(sql)
# db.commit()

# 删
# sql = 'delete from pythonTable WHERE age= %d'
# cursor.execute(sql % (12))
# db.commit()

# 改
# sql = 'update pythonTable set name="%s" WHERE age = "%d"'
# cursor.execute(sql % ('fengqi',13))
# db.commit()

sql = 'select * from pythonTable'
cursor.execute(sql)
results = cursor.fetchall()
print(results)
for row in results:
    print('姓名是:',row[0])
    print('年龄是:',row[1])
    print('爱好是:',row[2])