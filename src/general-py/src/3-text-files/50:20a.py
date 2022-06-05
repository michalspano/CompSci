file=open("news.txt", "r")
chr1=open("characters1.txt", "w")
chr2=open("characters2.txt", "w")

n=[]
char1=()
char2=()
for i in file:
  n.append(i.strip())
for x in n:
  for i in range(0,len(x)-1,2):
    char1+=(x[i],)
    char2+=(x[i+1],)

for ch1 in char1: #enables to write tuple/list to txt.
  chr1.write(ch1)
for ch2 in char2:
  chr2.write(ch2)
chr1.close()
chr2.close()


  
