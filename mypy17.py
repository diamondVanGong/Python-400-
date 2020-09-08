def print_star(n):
    print("*"*n)
print(print_star)
print(id(print_star))
c=print_star
c(3)
#测试函数也是对象
def test01():
    print("sxtsxtsxt")
test01()
c=test01
c()
#函数是对象，可以作为参数值传递，也可以作为返回值来返回
