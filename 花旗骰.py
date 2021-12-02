from random import randint
'''''''''
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
'''''''''
''''''
花旗色如第一次玩家7点和第一次以后7点相矛盾
''''''


def yaoshaizi():
    print('开始摇色子')
    number = randint(1,6) + randint(1,6)
    print('点数%d'%number)
    return number

def panduan(count,money,debet,number):
    if count==1:

        if number==7 or number==11:
            print('你赢了')
            money+=debet
            return money

        elif number==2 or number==3 or number==11:
            print("你输了")
            money-=debet
            return money

        else:
            print("继续摇色子")
            money+=0
            return money


    else:

         if number1==number:
             print('你赢了')
             money += debet
             return money

         elif number==7:
             print('你输了')
             money-=debet
             return money
         else:
             print('继续摇色子')
             money +=0
             return money

gamestart=input('输入y开始游戏：')
while gamestart=='y':
    money=int(input('你有多少钱:'))
    count = 1
    while count==1 and money>0:

            debet=int(input('你压多少钱：'))
            if debet>money:
                print('你钱不够')
            else:
                number=yaoshaizi()
                money=panduan(count,money,debet,number)
                number1=number
                count += 1
                print('你的第一次点数%d'%number1)
                print('你还剩%d钱'%money)
    else:
           pass
    while count>1 and money>0:

            debet=int(input('你压多少钱：'))
            if debet>money:
                print('你钱不够')
            else:
                number=yaoshaizi()
                money=panduan(count, money, debet, number)
                count += 1
                print('你还剩%d钱'%money)
    else:
            print('你输了，你没钱了')



else:
    print('输入错误游戏结束')







