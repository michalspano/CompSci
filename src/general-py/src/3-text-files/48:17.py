file1=open("signedup.txt", "r")
file2=open("signedupnames.txt", "w")

n=[]
for line in file1:
  n.append(line.strip())

for i in range(0,len(n),2):
  name=n[i]
  file2.write(str(name)+"\n")

file1.close()
file2.close()
