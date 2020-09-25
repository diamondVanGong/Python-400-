#测试调试断点
def aa():
    print("run in aa() satrt!")
    print("step1")
    num1=3
    num2=num1*4
    num3=num2*5
    print("step2")
    print("run in aa() end!!!")

if _name_=="_main_":
    print("main:step1: ")
    aa()
    print("main:step2")
    print("main;end1!!")
