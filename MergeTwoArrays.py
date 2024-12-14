# Raw Python Program (without in-built methods):
# Function to merge two arrays
def merge_arrays(arr1, arr2):
    merged_array = []
    
    # Add elements from the first array
    for item in arr1:
        merged_array.append(item)
    
    # Add elements from the second array
    for item in arr2:
        merged_array.append(item)
    
    return merged_array

# Input arrays
arr1 = [int(x) for x in input("Enter elements of the first array separated by space: ").split()]
arr2 = [int(x) for x in input("Enter elements of the second array separated by space: ").split()]

merged_array = merge_arrays(arr1, arr2)
print("Merged Array:", merged_array)

# Python Program with In-built Method (Using + operator):# Function to merge two arrays using in-built method
def merge_arrays(arr1, arr2):
    return arr1 + arr2  # Using the + operator to merge arrays

# Input arrays
arr1 = [int(x) for x in input("Enter elements of the first array separated by space: ").split()]
arr2 = [int(x) for x in input("Enter elements of the second array separated by space: ").split()]

merged_array = merge_arrays(arr1, arr2)
print("Merged Array:", merged_array)
