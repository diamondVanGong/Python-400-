#方法的多态，属性是没有堕胎的
#多态
class Man:
    def eat(self):
        print("饿了吗！！吃饭啦！！")

class Chinese(Man):
    def eat(self):
        print("中国人用筷子！")
class English(Man):
    def eat(self):
        print("英国人用叉子吃饭！")
class Indian(Man):
    def eat(self):
        print("印度人用右手吃饭")
def manEat(m):
    if isinstance(m,Man):
        m.eat()
#多态，一个方法调用，根据对象的不同调用过得方法也是不同的方法
    else:
        print("不能够吃饭！！")
manEat(Chinese())
manEat(English())