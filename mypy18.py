#测试全局变量，局部变量
a=3#全局变量
def test01():
    b=4
    print(b*10)
    print(a)
    global a#如果要在函数的内部改变全局变量
    #的值，增加global关键字的声明
    a=300
    print(a)
    print(locals())#输出局部变量
    print(globals())#输出全局变量
test01()
test01()
print(b)#没有被定义，报错了
print(a)#没有global，为3
