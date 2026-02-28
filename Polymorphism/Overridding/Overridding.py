# Child redefines parent method

class Parent:
    def show(self):
        print("From Parent")

class Child(Parent):
    def show(self): # Here Child redefines parent same method
        print("From Child") # Overrides parent
        super().show()

obj = Child()
obj.show()   # Output: From Child