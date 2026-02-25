"""class Myclass:
    def m1(self):
        print("instance method")
        print("instance method", self)

    @staticmethod
    def m2(self, Num):
        print(self, Num)
Myclass()
MC = Myclass()

MC.m1()
MC.m2(1, 2)

Myclass.m2(3, 4)
Myclass.m1(1)
GV1, GV2 = 10, 20
LV1, LV2 = 4, 8

class Variables:
    CV1, CV2 = 1, 2

    def instancemethod(self, LV1, LV2):
        print(GV1+GV2)
        print(LV1+LV2)
        print(self.CV1+self.CV2)
        print(LV1+LV2)
        print(globals()['LV1']+globals()['LV2'])

VC = Variables()
VC.instancemethod(5, 10)

class Constructor:
    CV = 12

    def __init__(self, a, b, c):
        self.A=a
        self.B=b
        self.C=c

    def display(self, d):
        print(self.A+self.B+self.C+d)

CC1 = Constructor(2, 3, 4)
CC1.display(6)

CC2 = Constructor(6, 7, 8)
CC2.display(9)
"""

class Test:
    def function1(self, b):
        self.a = b
        print("function1:", self.a)

    def function2(self):
        print("function2:", self.a)

obj = Test()
obj.function1(6)
obj.function2()
















