#测试运算符的重载
class Person:
    def _init_(self,name,age):
        self.name=name
        self._age=age
    def _str_(self):
        '''将对象转化成为一个字符串，一般用于print方法'''
        return "名字是:{0},年龄是{1}".format(self.name,self._age)
    def  _add_(self,other):
        if isinstance(other,Person):
            return self.name+other.name
        else:
            return "不是同类对象，不能够相加"
    def _mul_(self,other):
        if instance(other,Person):
            return "{0}---{1}".format(self.name,other.name)
        else:
            return "不是同类对象，不能够相加!"

p1=Person("gaoqi",32)
p2=Person("gaoxixi",6)
x=p1+p2
print(x*30)
