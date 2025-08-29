# ====Raw method(it means no ib-built function or methonds)=====

# Function to find common elements in two lists
def common_elements_no_builtin(list1, list2):
    common = [] # 2, 3, 4, 5, 6
    for i in range(len(list1)):  # First list loop # 1; 2;
        for j in range(len(list2)):  # Second list loop # 2, 3, 5;
            if list1[i] == list2[j]:
                already_present = False
                for k in range(len(common)):
                    if list1[i] == common[k]:
                        already_present = True
                        break
                if not already_present:
                    common.append(list1[i])
    return common

# Example:
list1 = [1, 2, 3, 4, 3]
list2 = [2, 3, 5]
print("Common Elements (No Built-in):", common_elements_no_builtin(list1, list2))


# ====with in-built method =================

# Function to find common elements in two lists using set

def common_elements_with_builtin(list1, list2):
    return list(set(list1) & set(list2)) # and

# Example:
list1 = [1, 2, 3, 4, 2]
list2 = [2, 3, 5]
print("Common Elements (With Built-in):", common_elements_with_builtin(list1, list2))

#  Another version (in-built in usage + no sets):

common_list =[]
list1 = input("Enter the list1 values: ")
list2 = input("Enter the list2 values: ")
for i in list1:
    if i in list2 and i not in common_list:
        common_list.append(i)
print(common_list)
