numbers = [1, 2, 3, 4]

print(all(numbers)) #True, because all values are truthy

numbers = [1, 2, 0, 4]

print(all(numbers)) #False, because 0 is a falsy value

marks = [80, 75, 20, 90, 85]

result = all(mark >= 35 for mark in marks)

print(result)  #False, because 20 is < 35