textfile=open("signedup.txt", "r")

price=int(input("Price?"))
lineCount=0
lines=()
for line in textfile:
  lineCount+=1
  lines=lines+(line.strip(),)
textfile.close

#a), number
pSigned=lineCount/2
print("Number of people signed: " + str(pSigned))

#b), less than 15
less15=0
avg_age=()
for i in range(0,len(lines),2):
  age=lines[i+1]
  age=int(age)
  if age<15:
    less15+=1
  avg_age+=(age,)
print("Number of people whose age is less than 15: "+str(less15))

#c); regular price = input
total=((pSigned*price)-(less15*(price/2)))
print("Price together: " + str(total))

#d), avg
avgTotal=0
varAvg=0
for x in range(0,len(avg_age),2):
  avgTotal+=(avg_age[x])+(avg_age[x+1])

varAvg+=len(avg_age)
average=avgTotal/varAvg
print("Average age: "+str(average))
  
