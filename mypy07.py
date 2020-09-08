#测试嵌套循环
for x in range(5):
    for y in range(5):
        print(x,end="\t")
    print("\n")
#打印9*9乘法表
for m in range(1,10):
    for n in range(1,m+1):
        print("{0}*{1}={2}".format(m,n,(n*m)))
    print()#换行
#使用列表和字典存储表格的数据
tb=[]
r1=dict(name="高效益",age=18,salary=3000,city="北京")
r2=dict(name="高小二",age=19,salary=4000,city="上海")
r3=dict(name="高小三",age=20,salary=5000,city="广州")
tb=[r1,r2,r3]
for x in tb:
    if x.get("salary")>3000:
         print(x)


