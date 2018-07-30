# 常见的存储数据方式
# 1.内存存储:变量 优点:读写操作快 缺点:程序关闭 内存释放
# 2.文件存储:文件读写操作 优点:数据永久 缺点:读写操作麻烦
# # 数据库极为数据存储仓库
# 3.数据库存储:优点 数据永久 缺点:难度大

# 数据库按性质划分有两种:
# 1.关系型数据库:数据与数据之间有着紧密的联系
#     优点:可以进行多表查询 缺点: 删除维护麻烦
#         牵一发而动全身
# 2.非关系型数据库:数据与数据之间没有关系
#     优点:对数据进行增删维护简单 缺点:数据之间少了耦合性
#         一人吃饱 全家不饿 mongoDB redis

# 数据库按照使用规模划分
# 可以分为四个等级
# 1.大型数据库 一般用于大型商业公司 例如淘宝，京东
#     代表 Orcale
# 2.中型数据库 使用非常广泛的数据库
#     代表 SQLServer
# 3.小型数据库 一般用于小的产品公司或者公司内部数据库
#     代表 mysql
# 4。微型数据库 经常用于移动端
#     代表 sqlite

import  sqlite3
# 创建一个数据库
con = sqlite3.connect('myDB')
# 创建一个游标
# 使用游标对数据库进行增删改查等操作
cursor = con.cursor()
# 使用游标执行命令：创建一张表 如果不存在
cursor.execute('CREATE TABLE IF NOT EXISTS myTable(name text,age int) ')
con.commit()
# inser into 插入数据到指定的表中
# cursor.execute('INSERT INTO myTable VALUES ("Kitty",3)')
# con.commit()
# cursor.execute('DELETE FROM myTable WHERE name = "Tom"')
# con.commit()
# cursor.execute('UPDATE myTable SET name = "dingDang" WHERE name="Wudi"')
# con.commit()
# cursor.execute('UPDATE myTable SET name="悟空" , age=500 WHERE  name="Kitty"')
# con.commit()
# 查看所有数据
cursor.execute('SELECT * FROM myTable')
# 查看第一个值
# result = cursor.fetchone()
# 查看多条数据
# result = cursor.fetchmany(2)
# 查看所有数据
result = cursor.fetchall()
print(result)