# import sqlite3,random
# con = sqlite3.connect('phoneDB' )
# cursor = con.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTS phone(name text,price int,memory text,rom text,function text,count int)')
# con.commit()
#
# class Customer(object):
#     name = ''
#     price = ''
#     memory = ''
#     rom = ''
#     function = ''
#     count = ''
# class Seller(object):
#     @classmethod
#     def fullMyshop(cls):
#         name = ''
#         price = ''
#         memory = ''
#         rom = ''
#         function = ''
#         count = ''
#         nameList = ['华为','小米','锤子','oppo','vivo','苹果','一加']
#         priceList = [599,799,999,1099,1299,1699,1999,2499,2999,3499,3999,4999,5999]
#         memoryList = ['512KB','2G','4G','6G','8G']
#         romList = ['16G','32G','64G','128G','512G']
#         functionList = ['美颜手机','双卡双待','超长续航','高清音质','超性价比','娱乐专享','游戏专享']
#         countlList = [0,5,10,20,100]
#         for i in range(20):
#             cursor.execute('INSERT INTO phone(name,price,memory,rom,function,count) VALUES ("{}","{}","{}","{}","{}","{}")'.format(random.choice(nameList),random.choice(priceList),random.choice(memoryList),random.choice(romList),random.choice(functionList),random.choice(countlList)))
#         con.commit()
#
#     @classmethod
#     def findPhone(cls,other):
#         cursor.execute('SELECT * FROM phone WHERE name = "{}" AND price<="{}" '.format(other.name,other.price))
#         result = cursor.fetchall()
#         for i in result:
#             cursor.execute('DELETE FROM phone WHERE name = "{}" AND count = 0'.format(other.name))
#             con.commit()
#         cursor.execute('SELECT * FROM phone WHERE name = "{}" AND price<="{}" '.format(other.name, other.price))
#         print(cursor.fetchall())
#         con.commit()
# # Seller.fullMyshop()
# Customer.name = '华为'
# Customer.price = '10000'
# Seller.findPhone(Customer)
#
# cursor.close()
# con.close()

# 再练习一遍
# import sqlite3,random
#
# con = sqlite3.connect('phoneDB1')
# cursor = con.cursor()
# cursor.execute('create table if not exists phoneInfo(name text,price INT ,memory text,rom text,function text,count INT )')
# class Customer(object):
#     name = ''
#     price = ''
#     memory = ''
#     rom = ''
#     function = ''
#     count = ''
# class Seiller(object):
#
#     @classmethod
#     def fullMyshop(cls):
#         nameList = ['小米', '一加', '华为', '苹果', 'oppo', 'vivo', '雷蛇', '美图', '锤子']
#         priceList = [599, 799, 999, 1299, 1999, 2999, 3499, 4999, 5999]
#         memoryList = ['512KB', '1G', '2G', '4G', '6G', '8G']
#         romList = ['16G', '32G''64G', '128G', '256G']
#         functionList = ['影音', '游戏', '美颜', '续航', '三防', '性价比']
#         for i in range(20):
#             cursor.execute('insert into phoneInfo(name,price,memory,rom,function,count) VALUES ("{}","{}","{}","{}","{}","{}")'.format(random.choice(nameList),random.choice(priceList),random.choice(memoryList),random.choice(romList),random.choice(functionList),random.randint(0,5)))
#             con.commit()
#
#     @classmethod
#     def find(cls,other):
#         result = cursor.execute('SELECT * FROM phoneInfo WHERE name = "{}" AND price < {}'.format(other.name,other.price))
#         for i in result:
#             print(i)
#         cursor.execute('DELETE FROM phoneInfo WHERE name="{}" AND count = 0'.format(other.name))
#         con.commit()
#         result = cursor.execute('SELECT * FROM phoneInfo WHERE name = "{}" AND price < {}'.format(other.name, other.price))
#         print('删除数量为0后:')
#         for i in result:
#             print(i)
# # Seiller.fullMyshop()
# Customer.name = '雷蛇'
# Customer.price = 5000
# Seiller.find(Customer)
