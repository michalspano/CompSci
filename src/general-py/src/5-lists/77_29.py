from random import *
my_list = [int(randrange(10**3, 10**4)) for i in range(8)]

current_min_element = my_list[0]
current_max_element = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] >= current_max_element:
        current_max_element = my_list[i]
    if my_list[i] <= current_min_element:
        current_min_element = my_list[i]

print(f"Max. element in: {my_list} : {current_max_element}")
print(f"Min. element in: {my_list} : {current_min_element}")
