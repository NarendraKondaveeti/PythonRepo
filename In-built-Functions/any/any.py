"""any() actually returns a boolean value. During iteration, it checks each element one by one. As soon as it finds the first truthy value, it immediately returns True without checking the remaining elements. If no truthy value is found, it returns False.

Telugu:Idi iterable lo unna values ni okkokatiga check chestundi.

Okka value aina True (truthy) unte, remaining values ni check cheyyakunda immediately True return chestundi.
Anni values False (falsy) ayithe matrame, False return chestundi.

"""

#============Examples:
numbers = [0, 0, 5, 0]

print(any(numbers)) #True, because 5 is a truthy value

numbers = [0, False, None, "", [], {}]

print(any(numbers)) #False, because all values are falsy

numbers = [False, "", [], {}, 100]

print(any(numbers)) #True, because 100 is a truthy value

numbers = [2, 4, 6, 8]

result = any(num % 2 != 0 for num in numbers)

print(result)  #False, because all numbers are even

marks = [35, 28, 60, 15]

result = any(mark >= 35 for mark in marks)

print(result)  #True, because 35 and 60 are >= 35

numbers = [0, 10, 25, -5, 40]

result = any(num > 0 for num in numbers)

print(result)  #True, because 10, 25, and 40 are positive