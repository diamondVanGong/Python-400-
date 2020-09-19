#测试工厂模式和单例模式的整合使用
class CarFactortory:
    #类属性
    _obj=None
    _init_flag=True
    def create_car(self):
        if brand=="奔驰":
            return Benz()
        elif brand=="宝马":
            return BMW()
        elif brand=="比亚迪":
            return BYD()
        else:
            return "未知品牌，无法创建"

    def _new_(cls, *args, **kwargs):
        if cls._obj == None:
             cls._obj = object._new_(cls)
        return cls._obj

    def _init_(self):
        if CarFactory._init_flag:
            print("init  CarFactory.....")
            self.name = name
            CarFactory._init_flag = False
class Benz:
    pass
class BMW:
    pass
class BYD:
    pass
factory=CarFactory()
c2=factory.create_car("比亚迪")
print(c1)
print(c2)

factory2=CarFactory()
print(factory)
print(factory2)





