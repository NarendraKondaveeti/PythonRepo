"""
with enumerate() function we can give the index for elements which is in the list or
any iterable(like string, tuple, set, dictionary)

Syntax:
enumerate(iterable, start = 0)
"""
EmpList = []
List = [10, 20, 30, 40]
print(list(enumerate(EmpList))) # []
print(enumerate(List))          # <enumerate object at 0x000001DBAB83D800>
print(list(enumerate(List)))    # [(0, 10), (1, 20), (2, 30), (3, 40)]
print(set(enumerate(List)))     # {(3, 40), (1, 20), (0, 10), (2, 30)}
print(tuple(enumerate(List)))   # ((0, 10), (1, 20), (2, 30), (3, 40))
print(dict(enumerate(List)))    # {0: 10, 1: 20, 2: 30, 3: 40}

for idx, i in enumerate(List):
    print(idx, i)

""" Output:-
0 10
1 20
2 30
3 40
"""

for idx, i in enumerate(List, start=1):
    print(idx, i)

""" Output:-
1 10
2 20
3 30
4 40
"""

""" zip() ============
zip() function allows you to combine multiple lists (or any iterables) into pairs of elements
it stops when the shortest iterable is exhausted
"""
List1 = [1, 2, 3]
List2 = ["Test", "API", "Automation"]
List3 = (10, 20, "Testing")
List4 = ["1st", "2nd"]
print(list(zip(EmpList))) # []
print(zip(List1, List2, List3)) # <zip object at 0x0000015F99013240>
print(list(zip(List1, List2, List3)))
# [(1, 'Test', 10), (2, 'API', 20), (3, 'Automation', 'Testing')]
print(set(zip(List1, List2, List3)))
# {(3, 'Automation', 'Testing'), (2, 'API', 20), (1, 'Test', 10)}
# print(dict(zip(List1, List2, List3)))
# ValueError: dictionary update sequence element #0 has length 3; 2 is required
print(list(zip(List1, List2, List3, List4))) # [(1, 'Test', 10, '1st'), (2, 'API', 20, '2nd')]

# enumerate() and zip() Together=======
print(enumerate(zip(List1, List2, List3))) # <enumerate object at 0x00000284BA63D580>
print(list(enumerate(zip(List1, List2, List3))))
# [(0, (1, 'Test', 10)), (1, (2, 'API', 20)), (2, (3, 'Automation', 'Testing'))]
"""for idx, i, j in enumerate(zip(List1, List2)):
    print(idx, i, j) 
    # ValueError: not enough values to unpack (expected 3, got 2)"""

for idx, (i, j) in enumerate(zip(List1, List2)):
    print(idx, i, j)
"""Output:-
0 1 Test
1 2 API
2 3 Automation
"""

for idx, i in enumerate(zip(List1, List2, List3)):
    print(idx, i)
"""Output:-
0 (1, 'Test', 10)
1 (2, 'API', 20)
2 (3, 'Automation', 'Testing')
"""