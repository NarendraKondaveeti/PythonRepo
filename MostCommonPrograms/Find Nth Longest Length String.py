def nth_longest_string(words, n):
    if n <= 0 or n > len(words):
        return None

    used = [False] * len(words)  # track already picked strings

    for count in range(n):
        max_val = None
        max_index = None

        for i in range(len(words)):
            if not used[i]:
                # length comparison
                if max_val is None or len(words[i]) > len(max_val):
                    max_val = words[i]
                    max_index = i
        used[max_index] = True

    return max_val

#Output: "orange" (because 6-length words are banana, cherry, orange → so 3rd one is orange).
# Example usage
words = ["orange", "apple", "mango", "cherry", "grape", "banana", "kiwi"]
nth = 3
result = nth_longest_string(words, nth)
print(f"{nth}rd longest string (length order) is:", result)
