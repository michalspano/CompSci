file1=open("file1.txt", "r")
file2=open("file2.txt", "w")

t=()
for line in file1:
  t+=(line.strip(),)
  
for i in range(len(t)):
  if t[i]!="":
    file2.write(t[i]+"\n")
file1.close()
file2.close()
