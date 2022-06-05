with open("input.txt","r") as textfile:
  n=[]
  for line in textfile:
    n.append(line.strip())

def palindromeCheck(n):
  output=[]
  lineOrder=input("Keep the line order?   y/n")
  for char in n:
    if char==char[::-1]:
      output.append(char)
    else:
      if lineOrder=="y":
        output.append("")
  return output

with open("output.txt", "w") as outputTextFile:
  for output in palindromeCheck(n):
    outputTextFile.write(output+"\n")
print("Function is completed, check your .txt file.")       
