#测试继承的基本使用
class Person:
    def _init_(self,name,age):
        self.name=name
        self._age=age
    def say_age(self):
        print("年龄，年龄，我不知道！")
class Student(Person):
    def _init_(self,name,age,score):
        Person._init_(self,name,age)
        #必须是显示的调用父类初始化，不然解释器不会去调用
        self.score=score
#私有属性子类继承了，但是不能够直接使用
#student-->Person-->object类
print(Student.mro())
s=Student("高淇",18,60)
s.say_age()
print(s.name)
print(s.age)
print(dir(s))
print(s._Person_age)