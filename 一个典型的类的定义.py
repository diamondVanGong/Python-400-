class Student:
    def _init_(self, name, score):  # 构造方法的第一个参数必须是self
        self.name = name  # 实例属性
        self.score = score

    def say_score(self):  # 实例方法
        print(self.name, '分数是:', self.score)


s1 = Student('张三', 80)  # s1是实例对象，自动调用_init_
s1 = say_score()
#通过类名（）调用构造函数
s1.age=32
s1.salary=3000
print(s1.salary)
s2=Student("gaoxixi",100)
s2.say_score(100)
Student.say_score(s2)
print(dir(s2))
print(isinstance(s2,Man))
class Man:
    pass
