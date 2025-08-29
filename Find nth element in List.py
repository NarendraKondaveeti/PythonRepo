def nth_largest(list, n):
    #max_val = None
    #max_index = -1
    if n <= 0 or n > len(list):
        return None
    used = [False] * len(list)
    for count in range(n):
        max_val = None
        max_index = -1
        for i in range(len(list)): #list length
            if not used[i]:
                if max_val is None or list[i] > max_val:
                    max_val = list[i]
                    max_index = i
        used[max_index] = True
    return max_val
list = list(map(int, input(f"Enter list number separated by space: ").split()))
#15 3 9 27 6 18
nth = int(input("Enter nth value:"))
result = nth_largest(list, nth)
print(f"The {nth}rd largest number is:", result)