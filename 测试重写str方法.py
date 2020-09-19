class Person:
    def _init_(self,name,age):
        self.name=name
    def _str_(self):
        return "名字是:{0}".format(self.name)
p=Person("高淇")
print(p)
