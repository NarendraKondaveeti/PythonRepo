data = None

while True:

    if data:
        print("Data Found:", data)
        break

    data = input("Enter data: ")
    print("Retrying...")