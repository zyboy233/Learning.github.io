import sqlite3
class Student(object):
    def __init__(self,name= '',age='',tel=''):
        self.name=name
        self.age=age
        self.tel = tel
class DBAction(object):
    def __init__(self,dbName,tableName):
        self.dbName = dbName
        self.tableName = tableName
        # 属性可以在类中任意使用
        self.con = None
        self.cursor = None
    def createDBAndTable(self):
        self.con = sqlite3.connect('{}'.format(self.dbName))
        self.cursor = self.con.cursor()
        self.cursor.execute('create table if not exists "{}"(name text,age text,tel text)'.format(self.tableName))
    def commitAndClose(self):
        self.con.commit()
        self.cursor.close()
        self.con.close()
    def openDB(self):
        self.con = sqlite3.connect('DBAction')
        self.cursor = self.con.cursor()
    def addNewStuToTable(self,stu):
        self.openDB()
        self.cursor.execute('insert into "{}" VALUES ("{}","{}","{}")'.format(self.tableName,stu.name,stu.age,stu.tel))
        self.commitAndClose()
    def updateStuToTable(self,stu):
        self.openDB()
        self.cursor.execute('update "{}" set NAME ="{}",age = "{}",tel ="{}"'.format(self.tableName,stu.name,stu.age,stu.tel))
        self.commitAndClose()
    def selectStuToTable(self):
        self.openDB()
        self.cursor.execute('select * from "{}"'.format(self.tableName))
        print(self.cursor.fetchall())
        self.commitAndClose()
    def delStuToTable(self,stuName):
        self.openDB()
        self.cursor.execute('delete from "{}" WHERE name = "{}"'.format(self.tableName,stuName))
        self.commitAndClose()

mydb = DBAction('DBAction','tableAction')
mydb.createDBAndTable()
# mydb.commitAndClose()

while True:
    value = int(input("""
    请输入指令:
    1.增加学生信息
    2.修改学生信息
    3.删除学生信息
    4.查看所有学生信息
    """))
    if value == 1:
        name = input('请输入姓名:')
        age = input('请输入年龄:')
        tel = input('请输入联系方式:')
        stu = Student(name,age,tel)
        mydb.addNewStuToTable(stu)
    elif value == 2:
        name = input('请输入你要修改学生的姓名:')
        name = input('请输入姓名:')
        age = input('请输入年龄:')
        tel = input('请输入联系方式:')
        stu = Student(name, age, tel)
        mydb.updateStuToTable(stu)
    elif value == 3:
        name = input('请输入要删除学生的姓名:')
        mydb.delStuToTable(name)
    elif value == 4:
        mydb.selectStuToTable()
    else:
        break