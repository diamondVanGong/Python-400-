#测试自定义异常类
class AgeError(Exception):#继承Exception
    def __init__(self,errorInfo):
        Exception._init_(self)
        self.errorInfo=errorInfo
    def _str_(self):
        return str(self.errorInfo)+",年龄错误,应该在1-159之间"
#########测试代码###############
if _name_=="main":#如果为True,则模块是作为独立文件运行的，
    #可以执行测试代码
    age=int(input("输入一个年龄:"))
    if age<1 or age>50:
        raise AgeError(age)
    else:
        print("正常的年龄",age)


