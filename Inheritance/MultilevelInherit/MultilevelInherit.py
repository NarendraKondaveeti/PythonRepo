# Multi-Level Inheritance Example

class Parent:
    p1, p2 = 10, 20
    def parentmethod(self):
        print(f"I'm from Parent class and values are {self.p1}, {self.p2}")

class Child(Parent):
    c1, c2 = 30, 40
    def childmethod(self):
        print(f"I'm from Child class and values are {self.c1}, {self.c2}")

class GrandChild(Child):
    g1, g2 = 50, 60
    def grandchildmethod(self):
        print(f"I'm from GrandChild class and values are {self.g1}, {self.g2}")

# Create object of GrandChild
obj = GrandChild()
# Access methods from all levels
obj.grandchildmethod()   # From GrandChild
obj.childmethod()        # From Child
obj.parentmethod()       # From Parent