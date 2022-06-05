n=input("Sum of digits: ")

def DigitSum(n):
  s=[]
  output=0
  for Int in n:
    s.append(Int)
  i=0
  while i < len(s):
    output+=int(s[i])
    i+=1
  return output
print("Output: "+str(DigitSum(n)))
    
