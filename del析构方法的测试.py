#析构方法的测试
class Person:
    del _del_(self):
        print("销毁对象{0}".format(self))
p1=Person()
p2=Person()
del p2
print("程序结束")
print(p1)
print(p2)

