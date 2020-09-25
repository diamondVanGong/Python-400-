#测试try...except...else的结构
try:
    a = input("请输入被除数:")
    b = input("请输入除数:")
    c = float(a) / float(b)
except BaseException as e:
    print(e)
else:
    print("除的结果是:", c)
