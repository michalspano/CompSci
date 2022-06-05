with open("example.txt", "r") as inputTextFile:
    n = [int(line) for line in inputTextFile]


def my_functions(n):
    sum_value = int()
    for value in n:
        sum_value += value
    average = sum_value / len(n)
    return sum_value, average


output = my_functions(n)
print(f"Sum: {output[0]}, check: {sum(n)}.")  # output in function + predetermined f.
print(f"Average: {output[1]}, check: {sum(n)/len(n)}.")  # output in function + predetermined f.
