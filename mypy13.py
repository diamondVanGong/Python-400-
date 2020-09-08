#测试推导式
#列表推导式
y=[x*2 for  x in range(1,5)if x%5==0]
print(y)

y=[]
for x in range(1,50):
    if x%5==0:y.append(x*2)
print(y)
cells=[(row,col) for row in range(1,10) for col in range(1,10)]
#使用两个循环




#字典推导式
mytext="i love you ,i love sxt,i love gaoqi"
char_count={for c in my_text.count(c) for c in my_text}
print(char_count)
#课下作恶，使用普通的循环实现上面字典推导式实现的字符出现的次数的统计
#生成器推导式（生成元祖）
gnt=（x for x in range(4))
print(gnt)
print(tuple(gnt))#(0,1,2,3)
print(tuple(gnt))#()
#生成器就是可迭代的对象
for x in gnt:#gnt是生成器对象
    #生成器是可迭代的对象,只能够使用一次
    print(x,end=",")
print(tuple(gnt))


