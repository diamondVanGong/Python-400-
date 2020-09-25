def test01():
    print("step1")
    try:
        x=3/0
        #return "a"
    except:
        print("step2")
        print("异常:0不能欧做除数")
        #return "b"
    finally:
        print("step4")
        #return "d"
    print("step5")
    return "e"
#一般不要将return语句放到try,except,else，finally快当中，会发生一些意想不到的错误，建议放到方法的最后
print(test01())