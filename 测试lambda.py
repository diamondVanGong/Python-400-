#测试lambda表达式，匿名函数
lambda a,b,c,d:a*b*c*d
def test01(a,b,c,d):
    return a*b*c*d;
printf(f(2,3,4,5))
g=[lambda a:a*2,lambda b:b*3]
printf(g[0](6))
h=[test01,test01]
printf(h[0](3,4,5,6))
#函数也是对象
