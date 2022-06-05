n = []
with open("cities1.txt", "r") as inputTextFile:
    for line in inputTextFile:
        n.append(line.strip())
my_list = [n[i].split(";") for i in range(len(n))]
countries_list = [my_list[i][1] for i in range(len(my_list))]
countries_list.sort()

with open("countries.txt", "w") as outputTextFile:
    for country in countries_list:
        outputTextFile.write(country + "\n")
