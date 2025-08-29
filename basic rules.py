def nth_largest(nums, n):
    #max_val = None
    #max_index = -1
    if n <= 0 or n > len(nums):
        return None
    used = [False] * len(nums)
    for count in range(n):
        max_val = None
        max_index = -1
        for i in range(len(nums)): #list length
            if not used[i]:
                if max_val is None or nums[i] > max_val:
                    max_val = nums[i]
                    max_index = i
        used[max_index] = True
    return max_val
list = [15, 3, 9, 27, 6, 18]
nth = 4
result = nth_largest(numbers, nth)
print(f"The {nth}rd largest number is:", result)
