# Example: Hierarchical Inheritance Practice

class Parent:
    p1, p2 = 10, 20
    def parentmethod(self):
        print(f"I'm from Parent class and values are {self.p1}, {self.p2}")

class Child1(Parent):
    c1, c2 = 30, 40
    def child1method(self):
        print(f"I'm from Child1 and values are {self.c1}, {self.c2}")

class Child2(Parent):
    d1, d2 = 50, 60
    def child2method(self):
        print(f"I'm from Child2 and values are {self.d1}, {self.d2}")

# Object of Child1

obj1 = Child1()
obj1.child1method()
obj1.parentmethod()
print()
# Object of Child2

obj2 = Child2()
obj2.child2method()
obj2.parentmethod()
