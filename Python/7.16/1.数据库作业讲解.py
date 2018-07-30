import sqlite3

connect = sqlite3.connect('studentDB')
cursor = connect.cursor()
cursor.execute('create table if not exists student_info(name text,age INT ,phone INT )')
connect.commit()

def add_student_info_table():
    name = input('请输入学生姓名:')
    age = int(input('请输入学生年龄:'))
    phone = int(input('请输入学生手机:'))
    cursor.execute('insert into student_info VALUES ("{}",{},{})'.format(name,age,phone))
    connect.commit()

def delete_student_info_table():
    name = input('请输入要删除学生的姓名:')
    cursor.execute('DELETE FROM student_info WHERE name = "{}"'.format(name))
    connect.commit()
def update_student_info_table():
    # select = input('请输入你想要的操作: 0:全部修改 1:修改姓名')
    name = input('请输入你要更新的数据:')
    new_name = input('请输入新的姓名:')
    new_age = input('请输入新的年龄:')
    new_phone = input('请输入新的联系方式:')
    cursor.execute('UPDATE student_info SET name = "{}" , age = "{}",phone = "{}" where name = "{}"'.format(new_name,new_age,new_phone,name))
    connect.commit()
def get_all_info_from_table():
    cursor.execute('SELECT * from student_info')
    connect.commit()
    print(cursor.fetchall())

print("""
学生信息管理系统：
输入1：添加学生信息
输入2：修改学生信息
输入3：删除学生信
输入4：查询所有学生信息
输入其他数字：退出查询系统
""")
while True:
    value = int(input('请输入你要执行的命令:'))
    if value == 1:
        add_student_info_table()
    elif value == 2:
        update_student_info_table()
    elif value == 3:
        delete_student_info_table()
    elif value == 4:
        get_all_info_from_table()
    else:
        print('退出程序')
        break
# add_student_info_table()
# delete_student_info_table()
# update_student_info_table()
# get_all_info_from_table()

cursor.close()
connect.close()

# 内存管理
# 堆:
# 栈:
# 常量区:
# 全局区:
# 方法区:
# 代码里面的一切内容都放在内存中
# 对象用完以后要释放,否则会一直占用内存,造成系统/电脑性能下降
# 对象以什么样的准则释放内存?
# 管理内存的原则:
# 1.手动释放
    # C
# 2.自动释放
    # java 垃圾自动回收机制
# 3.引用计数
    # python oc