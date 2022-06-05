file1=open("coordinates.txt", "r")
file2=open("coordinates2.txt", "w")

t=()
for line in file1:
  t+=(line.strip(),)
for i in range(0,len(t),2):
  x=t[i]
  y=t[i+1]
  file2.write(str(x) + " " +str(y)+"\n")
file1.close()
file2.close()
  
  


  
