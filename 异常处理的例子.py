# 实例：循环输入数字，如果不是数字就处理异常，知道输入88就结束循环
while True:
    try:
        x = int(input("请输入一个数字"))
        print("请输入数字:")
        if x == 8:
            print("退出程序")
            break
    except BaseException:
        print(e)
        print("异常输入的不会一个数字")

print("循环数字输出入程序结束")

