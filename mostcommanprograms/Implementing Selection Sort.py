# ====Raw method(it means no ib-built function or methonds)=====
# Function to implement Selection Sort
def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Find the minimum element in unsorted part of array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Input array
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

selection_sort(arr)
print(f"Sorted array: {arr}")


# ====with in-built method =================

# Function to implement Selection Sort using in-built methods
def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Find the minimum element using min() and get its index using index()
        min_elem = min(arr[i:])
        min_idx = arr.index(min_elem, i, n)
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Input array
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

selection_sort(arr)
print(f"Sorted array: {arr}")
