# ame method, different inputs
from sympy import multipledispatch


class Calc:
    def add(self, a=0, b=0, c=0):
        return a + b + c

obj = Calc()
print(obj.add())
print(obj.add(10, 20))
print(obj.add(10, 20, 30))


# Another example with String

class Human:
    def sayhello(self, name=None):
        if name is not None:
            print(f"Hello {name}")
        else:
            print("Hello")

H = Human()
H.sayhello("NK")

class A:
    @multipledispatch.dispatch(str)
    def display(self, String):
        print(f"test with string class method {String}")

class B(A):
    @multipledispatch.dispatch(int)
    def display(self, number):
        print(f"test with number class method {number}")

    @multipledispatch.dispatch(str)
    def display(self, String):
        super().display(String)

objB = B()
objB.display(5)
objB.display("Testing")

#singledispatch implementation need check more Here:-
from functools import singledispatch

@singledispatch
def process(x, y):
    return f"default: {type(x).__name__}, {x}, {y}"

@process.register(int)
def _(x: int, y):
    return f"int first: {x}, {y}"

@process.register(str)
def _(x: str, y):
    return f"str first: {x}, {y}"

@process.register(list)
def _(x: list, y):
    return f"list first (len={len(x)}): {x}, {y}"

print(process(10, "a")) # uses int implementation
print(process("hi", 5)) # uses str implementation
print(process([1,2], 3)) # uses list implementation
print(process(3.14, "x")) # uses default implementation