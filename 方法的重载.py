#Python当中没有方法的重载，定义多个同名的方法，只有最后一个是有效的
class Person:
    def say_hi(self):
        print("hello")
    def say_hi(self,name):
        print("{0}，hello".format(name))
p1=Person()
#p1.say_hi()
#不带参，报错，TypeError:say_hi()missing
