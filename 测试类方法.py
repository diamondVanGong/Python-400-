#测试类方法
class Student:
    company="SXT"
    def _init_(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def printCompany(cls):
        print(cls.company)
        #print(self.name)不能够这样子调用会报错的
Student.printCompany()
#类方法还有静态方法当中不能够调用实例变量还有实例方法
#测试静态的方法
class Student2:
    company="SXT"#类属性
    @staticmethod
    def add(a,b):#静态方法
        print("{0}+{1}={2}".format(a,b,(a+b)))
        return a+b
Student.add(20,30)