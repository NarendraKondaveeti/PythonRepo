"""
Tuple:-
Tuple is an immutable, its means once we create a tuple, we can not be changed (update/remove/add) elements into the tuple.
Tuple is ordered collection of elements, it means we can access the tuple elements with index
We can create a tuple with any type of data, it means, numbers, floats, strings, lists, set, tuples, dictionaries...
Tuple allows duplicate values
Tuple we can create in three ways
1. with parenthesis (), Tuple_Variable_Name = (elements)
2. Using tuple() constructor Tuple_Variable_Name = tuple(elements)
3. VariableName = element1,
# if we give comma after one value, then python will consider as tuple,
otherwise it will int, string based on given value

Positive index start with 0 end n-1
Negative index start with -1 end -n

if we concatenation two tuples with +, it will create new tuple,
it's not retain the memory address of tuple1 or tuple2

"""
EmpTuple = ()
print(type(EmpTuple)) # <class 'tuple'>
single_element = (10)
print(type(single_element)) # <class 'int'>
single_element_Str = ("Python")
print(type(single_element_Str)) # <class 'str'>
single_element_with_comma = (10,)
print(type(single_element_with_comma)) # <class 'tuple'>
single_element_Str_with_comma = ("Python",)
print(type(single_element_Str_with_comma)) # <class 'tuple'>
multiple_elements_without_parentheses = 1, 2, 3, "String1"
print(type(multiple_elements_without_parentheses))  # <class 'tuple'

Tuple = (1, 2, 3, "Test", "API", [1, 2, 3, "Postman"])
print(Tuple[1]) # 2
# Tuple[2] = 4  # TypeError: 'tuple' object does not support item assignment
print(len(Tuple)) # 5
print(Tuple[2])   # 3
print(Tuple[-2])  # API
print(Tuple[5][3]) # Postman
# Slicing =====
print(Tuple[1:3]) # (2, 3)
print(Tuple[1:3:-1]) # ()
print(Tuple[-1:3:-1]) # ([1, 2, 3, 'Postman'], 'API')

# concatenation ====
Tuple1 = (1, 2, 3)
Tuple2 = ("Test", "API", "Postman")
Tuple3 = Tuple1 + Tuple2
print(Tuple3) # (1, 2, 3, 'Test', 'API', 'Postman')
Tuple4 = (Tuple1, Tuple2)
print(Tuple4) # ((1, 2, 3), ('Test', 'API', 'Postman'))
print(Tuple4[1][1]) # API

for i in Tuple4:
    print(i)
"""Output:-
(1, 2, 3)
('Test', 'API', 'Postman')
"""

for j in range(len(Tuple3)):
    print(Tuple3[j])
"""Output:-
1
2
3
Test
API
Postman
"""

# enumerate() ====
EnuList1 = (1, 2, 3, "Test", "API", [1, 2, 3, "Postman"])
for idx, i in enumerate(EnuList1):
    print(idx, i)
"""Output:-
0 1
1 2
2 3
3 Test
4 API
5 [1, 2, 3, 'Postman']
"""

# Zip ====
ZipList1 = (1, 2, 3, "Test", "API", [1, 2, 3, "Postman"])
ZipList2 = (11, 12, 13, "API", [21, 22, "Postman"])
print(list(zip(ZipList1, ZipList2)))
# [(1, 11), (2, 12), (3, 13), ('Test', 'API'), ('API', [21, 22, 'Postman'])]