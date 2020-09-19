#测试nonlocal,global关键字的用法
def outer():
    b=10
    def inner():
        nonlocal b #声明外部函数的局部变量
        print("innner",b)
        #b=20直接b=20就会报错，必须要先声明一下
    inner()
    print("outer b:",b)
outer()
print("a:",a)
