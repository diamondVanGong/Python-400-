#测试浅拷贝，深拷贝
import copy
a=[10,20,[5,6]]
b=copy.copy()
print("a",a)
print("b",b)
b.append(30)
b[2].append(7)
print("浅拷贝:")
print("a",a)
print("b",b)

def testCopy():
    '''测试深拷贝'''
    a = [10, 20, [5, 6]]
    b = copy.deepcopy()
    print("a", a)
    print("b", b)
    b.append(30)
    b[2].append(7)
    print("浅拷贝:")
    print("a", a)
    print("b", b)
testDeepCopy()

