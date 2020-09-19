#测试私有属性:私有方法
class Employee:
    _company="百战程序员!"
    def _init_(self,name,age):
        self.name=name
        self._age=age#私有的属性
    def _work(self):#私有的方法
        print("好好工作，赚钱！！！")
        print("年龄:{0}".format(self._age))
        print(Employee._company)
e=Employee("高淇",19)
print(e.name)
print(e.age)
print(e._Employee_age)
print(dir(e))
e._Employee_work()
print(Employee._Employee_company)