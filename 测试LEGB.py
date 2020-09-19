#测试LEGB
print(str(30))
print(type(str))
#str="global str"
def outer():
    #str="outer"
    def inner():
        #str="inner"
        print(str)
        pass
    inner()
outer()
