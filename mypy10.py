#测试循环当中的else的语句
salarySum=0
salarys=[]
for i in range(4):
    s=input("请输入一共4名员工的薪资（按下Q或者q中途结束）")
    if s.upper()=='Q':
        print("录入已经完成，退出")
        break
    if float(s)<0:
        continue
    salarys.append(float(s))
    salarySum+=float(s)
else:
    print("您已经全部录入了4位员工的薪资!")
print("录入薪资:",salarys)
