class Student:
    company="SXT"#类属性
    count=0#类属性

    def _init_(self,name,score):
        self.name=name#实例属性
        self.score=score
        Student.count=Student.count+1
    def say_score(self):
        print("我的公司是:",Student.company)
        print(self.name,'的分数是',sel.score)
s1=Student('臧三',80)#s1是实例对象，自动调用_init()
s1.say_score()
s2=Student("高淇",60)
s3=Student("高松",100)
print('一共创建了{0}个Student对象'.format(Student.count))