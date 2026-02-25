#####Raw Python Program (without in-built methods):
# Function to sort an array manually
def sort_array(arr):
    # Loop through the array
    for i in range(len(arr)):
        # Find the smallest element in the unsorted part of the array
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                # Swap the elements
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Input array
arr = [int(x) for x in input("Enter numbers separated by space: ").split()]
sorted_array = sort_array(arr)
print("Sorted Array:", sorted_array)

#### Python Program with In-built Method (Using sort()):
# Function to sort an array using in-built method
def sort_array(arr):
    arr.sort()  # In-built method to sort the array
    return arr

# Input array
arr = [int(x) for x in input("Enter numbers separated by space: ").split()]
sorted_array = sort_array(arr)
print("Sorted Array:", sorted_array)
