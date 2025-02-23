# Shallow Copy =======

"""
Here, List1 and List2 have different memory addresses, they are not the same.
List2 is created separately, so if we update any value in List2,
it will not be reflected in List1.
However, in a shallow copy, there is one problem—if the original list contains a nested list,
the shallow copy does not create a new nested list; instead, it refers to the original nested list.
this same will happen in same in Dictionary, Tuple also

we can create shallow copy in three ways
1. copy_list_name = original_list_name.copy()  # Here we used .copy() in-built function
2. copy_list_name = list(original_list_name)   # Here we used list() list constructor in-built function
3. copy_list_name = original_list_name[:]      # Here we used slicing in-built function without giving any start, end, step values
the above three ways are same
"""


List1 = [1, 2, 3, "Test", "API"]
List2 = List1.copy()
print(id(List2)) != print(id(List1)) # List1 and List2 have different memory addresses, they are not the same

NestList1 = [1, 2, 3, "Test", "API",[4, "Playwright", "python"]]
NestList2 = NestList1.copy()
NestList2[5][0] = 1
print(NestList1) # [1, 2, 3, "Test", "API",[1, "Playwright", "python"]]
# Here in NestList1 of nested list element also reflected by NestList2[5][0] = 1,
# because shallow copy does not create a new nested list

Dict = {1: "Test", 2: "API", 3: "Automation", 4: {5: "Postman", 6: "Python"}}
Dict2 = Dict.copy()
print(id(Dict))
print(id(Dict2))
Dict[4][5] = "NewMan"
print(Dict2)

"""
Deep copy creates a completely new copy of the nested list. 
It does not take a reference from the original list. 
"""
from copy import deepcopy

DeepList1 = [1, 2, 3, "Test", "API",[4, "Playwright", "python"]]
DeepList2 = deepcopy(DeepList1)
# DeepList2 = copy.deepcopy(DeepList1) we can write like this way also
DeepList2[5][0] = 1
print(DeepList1) # [1, 2, 3, "Test", "API",[4, "Playwright", "python"]]
print(DeepList2) # [1, 2, 3, "Test", "API",[1, "Playwright", "python"]]