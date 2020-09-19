# 测试try和多个except的结构
try:
    a = input("请输入一个被除数")
    b = input("请输入一个除数:")
    c = float(a) / float(b)
    print(c)
except ZeroDivisionError:
    print("异常不能够除以0")
except ValueError:
    print("异常，不能够将字符串串转为数字")
except NameError:
    print("异常变量不存在")
except BaseException as e:
    print(e)

