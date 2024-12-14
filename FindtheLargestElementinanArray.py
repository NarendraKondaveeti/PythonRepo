# Raw Python Program (without in-built methods):

# Function to find the largest element in an array
def find_largest(arr):
    largest = arr[0]  # Assume the first element is the largest initially
    
    # Loop through the array
    for num in arr:
        if num > largest:
            largest = num  # Update the largest if we find a larger element
    
    return largest

# Input array
arr = [int(x) for x in input("Enter numbers separated by space: ").split()]
largest_element = find_largest(arr)
print("Largest Element:", largest_element)

# Python Program with In-built Method (Using max()):
# Function to find the largest element using in-built method
def find_largest(arr):
    return max(arr)  # Using the max() function to find the largest element

# Input array
arr = [int(x) for x in input("Enter numbers separated by space: ").split()]
largest_element = find_largest(arr)
print("Largest Element:", largest_element)
