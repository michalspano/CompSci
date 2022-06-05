def splitName(fullname):
  length=0
  output=[]
  position=fullname.split(" ")
  for x in fullname:
    if x==" ":
      length+=1
  for name in range(0,length+1):
    output.append(position[name])
  return output

names=splitName("Adam John Smart David Daniel Lukas")
for printOut in names:
  print(printOut)
