def nth_smallest(nums, n):
    if n <= 0 or n > len(nums):
        return None
    used = [False] * len(nums)
    for count in range(n):
        min_val = None
        min_index = None
        for i in range(len(nums)):
            if not used[i]:
                if min_val is None or nums[i] < min_val:
                    min_val = nums[i]
                    min_index = i
        used[min_index] = True
    return min_val


# Example usage
numbers = [15, 3, 9, 27, 6, 18]
nth = 4
result = nth_smallest(numbers, nth)
print(f"The {nth}rd smallest number is:", result)
