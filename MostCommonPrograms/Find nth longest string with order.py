def nth_longest_string(words, n):
    if n <= 0 or n > len(words):
        return None
    used = [False] * len(words)
    for count in range(n):
        max_val = None
        max_index = None
        max_len = -1
        for i in range(len(words)):
            if not used[i]:
                # Step 1: Compare based on length
                if (len(words[i]) > max_len) or (len(words[i]) == max_len and (max_val is None or words[i] < max_val)):
                    max_len = len(words[i])
                    max_val = words[i]
                    max_index = i
        used[max_index] = True  # Mark used
    return max_val
# Example usage
strings = ["banana", "orange", "cherry", "apple", "kiwi"]
nth = 3
result = nth_longest_string(strings, nth)
print(f"The {nth}rd longest string is:", result)


#=======Another Way==================
def nth_longest_string(words, n):
    # Sort words by (length, alphabetical order) in descending
    if n <= 0 or n > len(words):
        return None

    sorted_words = sorted(words, key=lambda x: (len(x), x), reverse=True)
    return sorted_words[n - 1] # ["orange", "cherry", "banana", "apple", "kiwi"]

# Example usage
strings = ["banana", "orange", "cherry", "apple", "kiwi"]
nth = 4
result = nth_longest_string(strings, nth)
print(f"The {nth}rd longest string is:", result)

