# define a class
#self源自于myself，当我们执行一个动作时，需要指定谁（self），完成什么动作self.动作
#self表面当前函数在那个对象上执行。隐式传递
from enum import Enum #Enum是一个类型，从enum中导入
import numpy as np
class gender(Enum):#继承语法 inherition
    male = 0
    female = 1
class person:
    "这是一个说明document,user defined class : person"
    #如果想创建一个对象，该对象会执行构造函数完成初始化
    def __init__(self, idno='N/A',name='N/A'):
    #一个构造函数，__init__有两个下划线，避免user重复命名
    #N/A是not available值没有给，默认参数
        self.sname = name#这个人的名字
        self.gender = gender.male#这个人的性别,from class 'gender'
        self.sid = idno
        self.iweight = 0
    
    def speak(self):
        print("person::speak():")
        print('i am',self.sname+',','nice to meet you')
    
    def eat(self,weight):
        self.iweight += weight
        print('i just eat', weight,'gram food.','i am',self.iweight,'gram now')
    
    def description(self):
        assert self.gender in (gender.female, gender.male)#assert 断言语法，如果写错了会提示
        s = 'id: %s \t name: %s\n'%(self.sid,self.sname)
        #t = 'gender: %s\tbody weight: %d'% ('male' if self.gender==)
        return s