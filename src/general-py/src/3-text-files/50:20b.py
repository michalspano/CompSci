input1=open("characters1.txt", "r")
input2=open("characters2.txt", "r")
result=open("charJoin.txt", "w")

t1=[]
t2=[]
t3=[]
t4=[]
output=""

for line1 in input1:
  t1.append(line1.strip())
for x1 in t1:
  for i in range(len(x1)):
    t3.append(x1[i])

for line2 in input2:
  t2.append(line2.strip())
for x2 in t2:
  for i in range(len(x2)):
     t4.append(x2[i])

for char in range(len(t3)): #or len(t4), they have the same len value;
  output+=t3[char]+t4[char]
result.write(output)
result.close()

