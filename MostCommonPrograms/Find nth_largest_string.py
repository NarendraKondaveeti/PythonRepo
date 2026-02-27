def nth_largest_string(words, n):
    if n <= 0 or n > len(words):
        return None
    used = [False] * len(words)
    for count in range(n):
        max_val = None
        max_index = None
        for i in range(len(words)):
            if not used[i]:
                if max_val is None or words[i] > max_val:
                    max_val = words[i]
                    max_index = i
        used[max_index] = True
    return max_val


# Example usage
strings = ["banana", "apple", "mango", "cherry", "grape", "orange"]
nth = 3
result = nth_largest_string(strings, nth)
print(f"The {nth}rd largest string is:", result)
#Output: "grape" (because in dictionary order: orange > mango > grape > cherry > banana > apple).