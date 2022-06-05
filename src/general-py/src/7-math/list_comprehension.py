n = [(number * 10 if number % 2 == 0 else number * 20) for number in range(20)]
print(n)

string = [len(word) for word in "My name is Michal".split()]
print(string)


def list_of_lists(arr):
    result = [list(range(0, number+1)) for number in arr]
    print(result)


list_of_lists([0, 2, 3, 2])
