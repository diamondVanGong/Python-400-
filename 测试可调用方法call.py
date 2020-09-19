# 测试可调用方法_call_()
class SalaryAccount:
    '''工资计算类'''

    def _call_(self, *args, **kwargs):
        print("算工资啦---")
        yearSalary=salary*12
        daySalary=salary//27.5
        #国家规定的每个月的平均工作天数
        hourSalary=daySalary//8
        return dict(yearSalary=yearSalary,monthSalary=salary,daySalary=daySalary,hourSalary=hourSalary)

s=SalaryAccount()
s = SalaryAccount()t
s(3000)
