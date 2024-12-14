# ====Raw method(it means no ib-built function or methonds)=====

# Function to implement Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Input array
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

bubble_sort(arr)
print(f"Sorted array: {arr}")

# ====with in-built method =================

# Function to implement Bubble Sort using in-built method (sort)
def bubble_sort(arr):
    arr.sort()  # Using in-built sort method

# Input array
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

bubble_sort(arr)
print(f"Sorted array: {arr}")
