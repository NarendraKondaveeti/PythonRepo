#Ex1:- Child redefines parent method
class Parent:
    def show(self):
        print("From Parent")

class Child(Parent):
    def show(self): # Here Child redefines parent same method
        print("From Child") # Overrides parent

obj = Child()
obj.show()   # Output: From Child
print("===Super keyword===")
#Ex2:-  Super keyword
class Parent:
    def show(self):
        print("From Parent")

class Child(Parent):
    def show(self): # Here Child redefines parent same method
        print("From Child") # Overrides parent
        super().show()

obj = Child()
obj.show()
print("===Direct Parent Call====")
#Ex3:- Direct Parent Call
class Parent:
    def show(self):
        print("From Parent")

class Child(Parent):
    def show(self): # Here Child redefines parent same method
        print("From Child") # Overrides parent
        super().show()

obj = Child()
Parent.show(obj)       # 👈 Parent method only
print("====Multi-Level Example====")
#Ex4:- Super keyword for Multi-Level Example

class A:
    def show(self):
        print("From A")

class B(A):
    def show(self):
        print("From B")
        super().show()

class C(B):
    def show(self):
        print("From C")
        super().show()

obj = C()
obj.show()
print("====Multiple Inheritance Example====")
#Ex5:- Super keyword for Multiple Inheritance Example
class A:
    def show(self):
        print("From A")
        super().display()

class B:
    def show(self):
        print("From B show")

    def display(self):
        print("From B display")

class C(A, B):
    def show(self):
        print("From C")
        super().show()

obj = C()
obj.show()
print("===Diamond Example====")
# Ex6:- Diamond Example
class A:
    def show(self):
        print("From A")
class B(A):
    def show(self):
        print("From B")
        super().show()
class C(A):
    def show(self):
        print("From C")
        super().show()
class D(B, C):
    def show(self):
        print("From D")
        super().show()
obj = D()
obj.show()