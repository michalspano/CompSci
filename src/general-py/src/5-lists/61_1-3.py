from random import *

rangeInput=int(input("Number of throws: "))
counts=[0]*6
i=0
while i <rangeInput:
  throw=randint(1,6)
  count=counts[throw-1]+1
  counts[throw-1]+=1
  i+=1
  print("So far there has been {} roll(s) of the number {}, with number of throw '{}'.".format(count,throw,i))
for i in range(6):
  print("The number {} was rolled {} times.".format(i+1,counts[i]))
print(counts)
with open("61_3.txt", "w") as textFileOutput:
  textFileOutput.write("Random sequence: ")
  for char in counts:
    textFileOutput.write(str(char)+" ")

