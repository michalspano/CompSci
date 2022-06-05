file1=open("score.txt", "r")
file2=open("score2.txt", "w")

count=0
for line in file1:
  count+=1
  file2.write(str(count)+". "+line)

file1.close()
file2.close()
