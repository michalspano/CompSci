print("51/23b - .txt to .html")
inp=input("Text file? ")

n=[]
with open(inp, "r") as inputFile:
  for line in inputFile:
    n.append(line)
    
split=inp.split(".")
name=split[0]+".html"

output=open(name, "w")
for char in n:
  output.write("<h1>"+char+"</h1>")
output.close()
  
