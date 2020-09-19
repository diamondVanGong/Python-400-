#测试继承的基本使用
class Person:
    def _init_(self,name,age):
        self.name=name
        self._age-age
        #私有属性
    def say_age(self):
        print("年龄，年龄我也不知道")
    def say_introduce(self):
        print("我的名字是{0}".format(self.name))
class Student (Person):
    def _init_(self,name,age,score):
        Person._init_(self,name,age)
        #必须是显示的调用父类初始化的方法，不然解释器不会去调用
        self.score=score
    def say_introduce(self):
        '''重写了父类的方法'''
        print("报告老师，我的名字是:{0}".format(self.name))
#Student--->Person->>object类
print(Student.mro())
a=Student("gaoqi",18,60)
a.say_age()
s=Student("高淇",18,80)
s.say_age()
s.say_introduce()