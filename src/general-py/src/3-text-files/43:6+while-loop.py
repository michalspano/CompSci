textfile=open("signedup.txt", "r")
price=int(input("Price?"))

t=()
for line in textfile:
  t+=(line.strip(),)

peopleCount=len(t)/2
print("Number of people who signed in: ",peopleCount)

age=[]
i=0
while i < len(t):
  ag=t[i+1]
  age.append(ag)
  age.sort()
  i=i+2

less15Count=0
for x in range(0,len(age)):
  while int(age[x]) < 15:
    less15Count+=1
    break
print("Number of people whose age is less than 15: ", less15Count)
total=(peopleCount*price)-(less15Count*(price/2))
print("Price together", total)

total=0
i=0
while i < len(age):
  total+=int(age[i])+int(age[i+1])
  i=i+2
print("Average age", total//peopleCount)
  


  

  
