
# 上期作业

class People(object):
    def __init__(self,name ='',sex = '',money = '',height = '',face = '',house_area='',house_value='',car_value='',win = ''):
        self.name = name
        self.sex = sex
        self.money = money
        self.height = height
        self.face = face
        self.house_area = house_area
        self.house_value = house_value
        self.car_value = car_value
        self.win = win
class Woman(People):
    #判断男方房中是否产生了赢家
    def isHasWin(self,man1,man2):
        if man1.win == False and man2.win == False:
            return False
        else:
            return True

    def choiceBoyFriendWithBoy(self,xiaowang,xiaoli):
        if xiaowang.money<1000000 and xiaoli.money<1000000:
            print('俩人都钱少')
        elif xiaowang.money<1000000 and xiaoli.money>=1000000:
            print('{}胜出'.format(xiaoli))
            return
        elif xiaowang.money>=1000000 and xiaoli.money<1000000:
            print('{}胜出'.format(xiaowang))
            return
        elif xiaoli.money > 10000000 and xiaoli.money > 10000000 and xiaoli.money>xiaowang.money:
            print('{}胜出'.format(xiaoli))
            return
        elif xiaoli.money > 10000000 and xiaoli.money > 10000000 and xiaoli.money<xiaowang.money:
            print('{}胜出'.format(xiaowang))
        # elif
class Man(People):
    def __init__(self,name,sex,money,height,face,house_area,house_value,car_value,win):
        super(Man,self).__init__(name,sex,money,height,face,house_area,house_value,car_value,win)

xiaoMei = Woman()
xiaoWang = Man('小王',True,1000000,169,7,100,200,50,False)
xiaoLi = Man('小李',True,100000,180,10,50,80,20,False)

# 传入两个被选择的对象
xiaoMei.choiceBoyFriendWithBoy(xiaoWang,xiaoLi)