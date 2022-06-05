user1 = input("Input visited cities separated by a space: ").split()
user2 = input("Input visited cities separated by a space: ").split()

output_list = []
for input1 in user1:
    if input1 in user2:
        output_list += [input1]

print("Cities visited by both users: ", ", ".join(repr(c) for c in output_list))
