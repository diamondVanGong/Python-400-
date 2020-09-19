class Student:
    #类名一般首字母大写，多个单词采用驼峰原则
    def _init_(self,name,score):#self必须位于第一个参数
        self.name=name
        self.score=score
    def say_score(self):#self必须位于第一个参数
        print("{0}的分数是:{1}".format(self.name,self.score))
stu2=Student
s1=Student("高淇",60)
s2=stu2("高希希",100)#结果是一摸一样的
