# Counter
from collections import Counter

output = []
n = [1, 2, 3, 2, 2]
for key, value in Counter(n).items():
    output.append([key, value])

print(output)
