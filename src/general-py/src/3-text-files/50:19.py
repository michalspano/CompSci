joinT=open("newsJoin.txt", "w")
input1=open("output1.txt", "r")
input2=open("output2.txt", "r")

t1=[]
t2=[]

for line1 in input1:
  t1.append(line1.strip())
for line2 in input2:
  t2.append(line2.strip())

for i in range(len(t1)):
  x1=t1[i]+"\n"
  x2=t2[i]+"\n"
  output=x1+x2
  joinT.write(output)
joinT.close()

