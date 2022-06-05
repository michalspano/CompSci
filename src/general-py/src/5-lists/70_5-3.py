answer = input("Enter the capital cities in the EU /n" +
               "you have visited (separate them using a space): ")

answer = answer.strip()
mylist = answer.split()
mylist.sort()
print("Number of cities visited: ", len(mylist))
print("Alphabetically sorted capital cities: ")
for city in mylist:
    print(city, end=" ")
