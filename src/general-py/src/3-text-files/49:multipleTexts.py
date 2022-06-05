##file_name=input("Input txt file: ")
##file_in=open(file_name, "r")
##output1=open("output1.txt", "w")
##output2=open("output2.txt", "w")
##where=0
##
##line=file_in.readline()
##
##while line !="":
##  if where %2 ==0:
##    output1.write(line)
##  else:
##    output2.write(line)
##  where=(where+1) 
##  print(where)
##  line=file_in.readline()
##
##file_in.close()
##output1.close()
##output2.close()
file=open("news.txt", "r")
output1=open("output1.txt", "w")
output2=open("output2.txt", "w")
t=()
for line in file:
  t+=(line.strip(),)
for i in range(0, len(t),2):
  output1.write(t[i]+"\n")
  output2.write(t[i+1]+"\n")
file.close()
output1.close()
output2.close()
