cities = input("Enter capital cities you visited separated by a space: ")\
    . split(" ")
w = ""
with open("cities1.txt", "r") as citiesTextFile:
    for city in citiesTextFile:
        w += city.strip() + " "
data = w.split(" ")
data = data[:-1]
d = [data[i].split(";") for i in range(len(data))]

capitalCities = [d[i][0] for i in range(len(d))]
countries = [d[j][1] for j in range(len(d))]

for answer in cities:
    if answer in capitalCities:
        capitalCities.remove(answer)
    else:
        print(f"{answer} not in list.")

print(f"Visited countries (number): {len(cities)}")
print(", ".join(repr(c) for c in cities))
print(f"Unvisited countries (number): {len(capitalCities)}")
print(", ".join(repr(cs) for cs in capitalCities))
