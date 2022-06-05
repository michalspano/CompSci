file=open("longline.txt", "r")
output=open("shortlines.txt","w")
length=int(input("Line length? "))

t=()
w=""

for line in file:
  t+=(line.strip(),)
for x in t:
  for i in range(len(x)):
    w+=(x[i])

amountOfLines=(len(x)//length)+1 #range of number of lines in for loop;
count=length
x=-(length) #x1 must be zero, thus / -x+x;
y=0 #y1 must be y, thus 0 + y;

for i in range(amountOfLines):
  x+=count
  y+=count
  result=w[x:y]+"\n"
  output.write(result)
output.close()


