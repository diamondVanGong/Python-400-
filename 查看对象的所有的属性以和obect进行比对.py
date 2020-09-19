class Person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    def say_age(self):
        print(self.name,"的年龄是:",self.age)
obj=object()
print(dir(obj))
s2=Person("高淇",18)
print(dir(s2))
