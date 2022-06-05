example="x@x.x"

#example with conditions
at1=example.split("@")
n1=[]
n1.append(at1[0])
a1=at1[1]
dotSplit1=a1.split(".")
for char in dotSplit1:
  n1.append(char)
lengthExample=len(n1)
#we can determine the truth by length of the example; where example contains 3 terms without '@', '.''

def isEmail(input1, lengthExample):
  at=input1.split("@")
  n=[]
  n.append(at[0])
  a=at[1]
  dot=a.split(".")
  for x in dot:
    n.append(x)
  count=""
  check=False
  for char in input1:
    if char=="." or char=="@": 
      count+=char

  if count=="@.": #when input contains @. in the same order and count==True
    if len(n)==lengthExample: #when len(input)=len(example)==True
      check=True
  return check
   
print(isEmail(input("Input: "), lengthExample))
      
