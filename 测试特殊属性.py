#测试特殊属性
class A:
    def aa(self):
        print("aa")
    def say(self):
        print("say  AAA")
class B:
    def bb(self):
        print("bb")
    def say(self):
        print("say BB")
class C(B,A):
    def _init_(self,nn):
        self.nn=nn
    def cc(self):
        print("cc")

c=C(3)
print(C.mro())
print(c._dict_)
print(c._class_)
print(C._bases_)
print(C.mro())
print(C.mro())
print(A._subclasses())
