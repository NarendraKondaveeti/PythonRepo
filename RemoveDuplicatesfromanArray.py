# Raw Python Program (without in-built methods):
# Function to remove duplicates from an array
def remove_duplicates(arr):
    unique_elements = []
    
    # Loop through the array
    for item in arr:
        if item not in unique_elements:
            unique_elements.append(item)  # Add item to unique_elements if not already present
    
    return unique_elements

# Input array
arr = [int(x) for x in input("Enter numbers separated by space: ").split()]
result = remove_duplicates(arr)
print("Array without duplicates:", result)

# Python Program with In-built Method (Using set()):
# Function to remove duplicates using in-built method
def remove_duplicates(arr):
    return list(set(arr))  # Convert the list to a set to remove duplicates, then back to a list

# Input array
arr = [int(x) for x in input("Enter numbers separated by space: ").split()]
result = remove_duplicates(arr)
print("Array without duplicates:", result)
