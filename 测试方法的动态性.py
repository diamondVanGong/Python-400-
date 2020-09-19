#测试方法的动态性
class Person:
    def work(self):
        print("努力上班!")
def play_name(s):
    print("{0}在玩游戏".format(s))
def work2(s):
    print("好好学习，努力上班，赚大钱，！")
Person.play=play_name;
p=Person()
p.work()
p.play_name()
p.play()
Person.work=work2
p.work()
