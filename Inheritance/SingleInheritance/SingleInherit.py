#Example1:-

class Parent:
    def parentmedthod(self):
        print("I'm from SingleInheritance of parentmedthod")

class Child(Parent):
    def childmedthod(self):
        print("I'm from SingleInheritance of childmedthod")

Child = Child()
Child.childmedthod()
Child.parentmedthod()
print("")
#Example2:-

class Parent2:
    p1, p2 = 10, 20
    def parentmedthod2(self, p3):
        print(f"I'm from SingleInheritance of parentmedthod2 and I have {self.p1}, {self.p2} and sum of those {self.p1+self.p2-p3}")

class Child2(Parent2):
    c1, c2 = 30, 40
    def childmedthod2(self):
        print(f"I'm from SingleInheritance of childmedthod2 and I too have {self.c1}, {self.c2}")

Child2 = Child2()
Child2.childmedthod2()
Child2.parentmedthod2(5)
