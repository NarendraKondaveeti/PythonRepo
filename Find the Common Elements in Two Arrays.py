# ====Raw method(it means no ib-built function or methonds)=====

# Function to find common elements in two arrays
def common_elements(arr1, arr2):
    common = []
    for element in arr1:  # Loop through each element in the first array
        if element in arr2:  # Check if the element is present in the second array
            common.append(element)  # Add the common element to the result list
    return common

# Input arrays
arr1 = list(map(int, input("Enter the first array (space-separated values): ").split()))
arr2 = list(map(int, input("Enter the second array (space-separated values): ").split()))

result = common_elements(arr1, arr2)
print(f"The common elements in the two arrays are: {result}")

# ====with in-built method =================

# Function to find common elements in two arrays using set
def common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))  # Use set intersection to find common elements

# Input arrays
arr1 = list(map(int, input("Enter the first array (space-separated values): ").split()))
arr2 = list(map(int, input("Enter the second array (space-separated values): ").split()))

result = common_elements(arr1, arr2)
print(f"The common elements in the two arrays are: {result}")
