
# 一女子择偶,两个男士被选择
# 1.如果两男存款少于100万,都不考虑
# 2.如果两男存款大于1000万,跟存款多的走
# 3.男士
# 4.选择个子高的
# 5.若果个子都大于170,且相差不到5厘米,看颜值(0,10)
# 7.低于7分的直接pass,高于7分选择颜值高的,若果颜值相差不到2,看房子
# 8.房子不能低于100平且价值不能少于200万,都有的话,选择价值高的
#     价值相差少于20万,看车子
# 9.车子价值不能少于50万,相差不到10万,抛硬币
#
# 使用继承
# 传入两个对象
# def 抛硬币()

import random
class Human(object):
    def __init__(self,name='',sex=True,height = 0):
        self.name = name
        self.sex = sex
        self.height = height

    def sexCunkuan(self,person1,person2):
        if person1.sex == person2.sex ==False or (person1.cunkuan and person2.cunkuan) in range(1000000):
            return 0
        if person1.sex ==person2.sex ==True:
            if (person1.cunkuan and person2.cunkuan) in range(1000000,10000001):
                return 1
            if (person1.cunkuan and person2.cunkuan) in range(10000000,):
                if person1.cunkuan>person2.cunkuan:
                    print('选择{}',format(person1.name))
                    return 2
                if person1.cunkuan<person2.cunkuan:
                    print('选择{}',format(person2.name))
                else:
                    return 1
            if person1.cunkuan>1000000 and person2<100000:
                return 2
            if person1.cunkuan<1000000 and person2>1000000:
                return 3
        if person1.sex == True and person2.sex == False:
            if person1.cunkuan in range(1000000,):
                return 2
            else:
                return 0

        if person1.sex == False and person2.sex == True:
            if person2.cunkuan in range(1000000,):
                return 2
            else:
                return 0
        else:
            return 3

    def isHeight(self,person1,person2):
        if ((person1.height and person2.height)<=170 and person1.height == person2.height) or ((person1.height and person2.height)>170 and abs(person1.height-person2.height)<=5):
            return 1
        if person1.height> person2.height:
            return 0
        if person1.height < person2.height:
            return 2

    def isPerfect(self,person1,person2):
        if (person1.perfect and person2.perfect) <7:
            return 0  #pass
        else:
            if abs(person1.perfect-person2.perfect)<2:
                return 1  #接着判断
            if person1.perfect>person2.perfect:
                return 0 #选择person1
            if person1.perfect<person2.perfect:
                return 2 #选择person2

    def isHouse(self,person1,person2):
        if (person1.house and person2.house)>100 and (person1.house_price and person2.house_price)>=2000000:
            if abs(person1.house_price-person2.house_price)<200000:
                return 0 #接着走
            if person1.house_price>person2.house_price:
                return -1 #选择person1
            if person1.house_price<person2.house_price:
                return 1 #选择person2
        if person1.house<100 and person2.house<100:
            print('你们房子都不行')
            return 2 #pass
        if person1.house>100 and person2.house<100:
            if person1.house_price>=2000000:
                return -1
            if person1.house_price<2000000:
                return 2 #pass
        if person1.house<100 and person2.house>100:
            if person2.house_price>=2000000:
                return 1
            if person2.house_price<2000000:
                return 2 #pass

    def isCar(self,person1,person2):
        if person1.car_price<500000 and person2.car_price<500000:
            return 0  #车都不行
        if abs(person1.car_price - person2.car_price)<100000:
            return  3
        if person1.car_price>500000 and person2.car_price<500000:
            return 1  #选择1
        if person1.car_price<500000 and person2.car_price>500000:
            return 2  # 选择2

    def throwRmb(self):
        return random.randint(1,3)
class Man(Human):
    def __init__(self,name,sex,height,cunkuan,perfect,house,house_price,car_price):
        super(Man,self).__init__(name,sex,height)
        self.cunkuan = cunkuan
        self.perfect = perfect
        self.house = house
        self.house_price = house_price
        self.car_price = car_price

class Woman(Human):
    def chose(self,man1,man2):
        result = super(Woman,self).sexCunkuan(man1,man2)
        if result == 0:
            print('存款问题或者性别不对')
        if result == 2 :
            print('选择{}'.format(man1.name))
        if result ==3:
            print('选择{}'.format(man2.name))
        if result == 1:
            result = super(Woman,self).isHeight(man1,man2)
            if result == 0:
                print('选择{}'.format(man1.name))
            if result == 2:
                print('选择{}'.format(man2.name))
            if result == 1:
                result = super(Woman,self).isPerfect(man1,man2)
                if result == 0:
                    print('颜值都不行')
                if result == 0:
                    print('选择{}'.format(man1.name))
                if result ==2:
                    print('选择{}'.format(man2.name))
                if result ==1:
                    result = super(Woman,self).isHouse(man1,man2)
                    if result == 2:
                        print('你们房子都不行')
                    if result == -1:
                        print('选择{}'.format(man1.name))
                    if result == 1:
                        print('选择{}'.format(man2.name))
                    if result == 0:
                        result == super(Woman,self).isCar(man1,man2)
                        if result == 1:
                            print('车都不行')
                        if result == 0:
                            print('选择{}'.format(man1.name))
                        if result == 2:
                            print('选择{}'.format(man2.name))
                        if result == 3:
                            result = super(Woman,self).throwRmb()
                            if result == 1:
                                print('选择{}'.format(man1.name))
                            else:
                                print('选择{}'.format(man2.name))

man1 = Man('张三',True,160,1200000,8,110,3000000,600000)
man2 = Man('李四',True,172,1100000,9,120,3000000,700000)
woman = Woman('小红',False,170)

woman.chose(man1,man2)