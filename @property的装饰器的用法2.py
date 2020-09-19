#@property的装饰器的用法:
class Employee:
    def _init_(self,name,salary):
        self._name=name
            self._salary=salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,salary):
        if 1000<salary<500000:
            self._salary=salary
        else:
            print("录入错误!薪水在1000-500000这个范围之内")
print(emp1.salary)
emp1.salary=-2000
print(emp1.salary)

