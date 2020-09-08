#测试形式参数和实际参数的基本用法
def printMax(a,b):
    '''用于比较两个数的大小，'''
    if a>b:
        print(a,"较大值")
    else:
        print(b,"较大值")
printMax(10,20)
printMax(200,300)
printMax()#报错，需要两个参数
printMax(200,300,400)#也是报错了
help(printMax._doc_)#调用文档字符串
