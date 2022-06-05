n = []
start = True

print("Assign values to delete / 'break' to terminate")


def rangeOfValues(n):
    global start
    while start:
        userInput = input("Input variables to delete: ")
        n.append(userInput)
        if userInput == "break":
            start = False
            n.remove(userInput)
    return n


rangeOfValues(n)

a = []
for i in range(int(input("Range of values")) + 1):
    a.append(str(i))
for number in rangeOfValues(n):
    a.remove(number)

# display to console
i = 0
while i < len(a):
    print(a[i])
    i += 1