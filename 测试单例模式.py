#测试单例模式
class MySingleton:
    _obj=None#类属性
    _init_flag=True
  def _new_(cls,*args,**kwargs):
        if cls._obj==None:
            cls._obj=object._new_(cls)
        return cls._obj
    def _init_(self,name):
        if MySingleton._init_flag:
            print("init.....")
            self.name=name
            MySingleton._init_flag=False
a=MySingleton("aa")
b=MySingleton("bb")
print(a)
print(b)
c=MySingleton("cc")
print(c)



