#测试函数返回值的基本的用法
def add(a,b):
    print("计算两个数的和:{0},{1},{2}".format(a,b,(a+b)))
    return a+b
def test02():
    print("sxt")
    print("b")
    return
    print("hello")
def test03(x,y,z):
    return [x*10,y*10,z*10]

#return两个作用1.返回值2.结束函数的执行
c=add(30,40)
print(add(30,40)*10)
d=test02()
print(d)#返回的None没有返回值也是的
print(test03(4,3,2))