def find_biggest_number(numbers):
    if len(numbers) == 0:
        return None  # Empty list case

    biggest = numbers[0]  # Assume first is biggest

    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest

# Example
numbers = [4, 9, 2, 15, 7, 1]
result = find_biggest_number(numbers)
print("Biggest number is:", result)
#===========================
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) == 0:
    print("No numbers entered.")
else:
    biggest = max(numbers)
    print("Biggest number is:", biggest)