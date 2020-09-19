#TraceBack追溯，追根溯源
def a():
    num=1/0
def b():
    a()
def c():
    b()
c()
---------------
print("step01")
try:
    print("step1")
    a=3/0
    print("step02")
except BaseException as e:
    print("step03")
    print(e)
    print(type(e))
print("end!!!!!")
    print("发生异常，0不能够做除数")

print("end!!!")