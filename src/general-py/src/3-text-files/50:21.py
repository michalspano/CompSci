#string not txt file/
##file=input("Input?" )
##shift=int(input("Shift? "))
##
##w=""
##for i in range(len(file)):
##  char=ord(file[i])
##  encr=(char+shift)
##  w+=str(chr(encr))
##print(w)

chFile=input("Input .txt file: ")
shift=int(input("Shift ?" ))
file=open(chFile,"r")
output=open("encryption.txt", "w")

t=[]
w=""
for char in file:
  t.append(char.strip()+"\n")

for x in t:
  for i in range(len(x)-1):
    char=x[i] 
    value=ord(char)
    encr=(value+shift)
    if encr > 122:
      encr=(encr-122)+97-1
    w+=str(chr(encr))
    
output.write(w)
output.close()
