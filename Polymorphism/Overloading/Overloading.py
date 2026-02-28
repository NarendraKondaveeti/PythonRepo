# ame method, different inputs
class Calc:
    def add(self, a=0, b=0, c=0):
        return a + b + c

obj = Calc()
print(obj.add())
print(obj.add(10, 20))
print(obj.add(10, 20, 30))
