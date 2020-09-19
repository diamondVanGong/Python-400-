class Employee:
    def _init_(self,name,salary):
        self._name=name
        self._salary=salary
    def get_salary(self):
        if 10000<salary<50000:
            return self._salary
        else:
            print("录入错误，薪水在1000-5000这个范围以内")
    def set_salary(self,salary):
        self._salary=salary

emp1=Employee("高淇",30000)
print(emp1._salary)#报错了，直接就是不可见了
emp1.salary=20000
print(emp1.salary)
print(emp1.get_salary())
emp1.set_salary(-20000)
print(emp1.get_salary())

