n=""
with open("article24.txt", "r") as inputT:
  for line in inputT:
    for x in line:
      n+=x
      
for i in range(len(n)-1):
  fChar=n[0].upper()
  if n[i]=="." or n[i]=="!" or n[i]=="?":
    char=n[i+2].upper()
    n=n[:i+2]+char+n[i+3:]
correction=(fChar+n[1:])
with open("article24-correction.txt", "w") as output:
  output.write(correction)      

    

    
    
