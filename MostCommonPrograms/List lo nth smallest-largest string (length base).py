#=====Without in-built sorted function

words = ["apple", "kiwi", "banana", "fig", "watermelon"]

n = 2

length = len(words)

for i in range(length):
    for j in range(length - i - 1):

        if len(words[j]) > len(words[j + 1]): #ikkada <(greater than symbol) istheye Nth Largest String find avuthundi,
            #Adeye >(less than symbol) istheye Nth smallest String find avuthundi,

            temp = words[j]
            words[j] = words[j + 1]
            words[j + 1] = temp

print(words[n-1])

#=====With in-built sorted function

words = ["apple", "kiwi", "banana", "fig", "watermelon"]

n = 2

sorted_words = sorted(words, key=len, reverse=False)#ikkada reverse=True istheye Nth Largest String find avuthundi,
            #Adeye reverse=False istheye Nth smallest String find avuthundi,
print(sorted_words)
result = sorted_words[n-1]

print(result)