# Example: Multiple Inheritance
class ParentA:
    a1, a2 = 10, 20
    def parentAmethod(self):
        print(f"I'm from ParentA and values are {self.a1}, {self.a2}")

class ParentB:
    b1, b2 = 30, 40
    def parentBmethod(self):
        print(f"I'm from ParentB and values are {self.b1}, {self.b2}")

class Child(ParentA, ParentB):
    c1, c2 = 50, 60
    def childmethod(self):
        print(f"I'm from Child and values are {self.c1}, {self.c2}")

# Create object of Child

obj = Child()

# Access methods from all parents + child

obj.childmethod()      # From Child
obj.parentAmethod()    # From ParentA
obj.parentBmethod()    # From ParentB

