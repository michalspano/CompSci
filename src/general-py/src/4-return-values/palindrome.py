#myFunction
##def palindrome(myinput):
##  if myinput!="" and myinput!=" ":
##    x1=0
##    x2=len(myinput)-1
##    result=True
##    while x1 < x2:
##      if myinput[x1]!=myinput[x2] and result:
##        result=False
##      else:
##        result=True
##      x1+=1
##      x2-=1
##    return result
##  else:
##    return "None"

##a) - False, local variable 'result' referenced before assignment
##def palindrome(myinput):
##  b=0
##  e=len(myinput)-1
##  while b<e:
##    if myinput[b]==myinput[e]:
##      result=True
##    else:
##      result=False
##    b+=1
##    e-=1
##  return result

#b) - false, local variable 'result' referenced before assignment
##def palindrome(myinput):
##  b=0
##  e=len(myinput)-1
##  while b<=e:
##    if myinput[b]==myinput[e]:
##      result=True
##    else:
##      result=False
##    b+=1
##    e-=1
##  return result

#c) - correct, but "" is not palindrom -> condition needed!
def palindrome(myinput):
  b=0
  e=len(myinput)-1
  result=True
  while b < e and result:
    if myinput[b]!=myinput[e]:
      result=False
    else:
      result=True  
    b+=1
    e-=1
  return result

#d) - false
##def palindrome(myinput):
##  b=0
##  e=len(myinput)-1
##  result=False
##  while b < e:
##    if myinput[b]==myinput[e]:
##      result=True
##    b+=1
##    e-=1
##  return result

#e) - false
##def palindrome(myinput):
##  b=0
##  e=len(myinput)-1
##  result=False
##  while b <= e:
##    if myinput[b]==myinput[e]:
##      result=True
##    b+=1
##    e-=1
##  return result

#f) - correct
##def palindrome(myinput):
##  result=True
##  for i in range(len(myinput)//2):
##    if myinput[i]!=myinput[-i-1]:
##      result=False
##  return result

#g) - correct
##def palindrome(myinput):
##  result=True
##  for i in range(len(myinput)):
##    if myinput[i]!=myinput[-i-1]:
##      result=False
##  return result

#h) - false
##def palindrome(myinput):
##  for i in range(len(myinput)):
##    if myinput[i]==myinput[-i-1]:
##      result=True
##    else:
##      result=False
##  return result
##  
#i) - false
##def palindrome(myinput):
##  result=False
##  for i in range(len(myinput)):
##    if myinput[i]==myinput[-i-1]:
##      result=True
##  return result
print("nolemonnomelon - ",palindrome("nolemonnomelon"))
print("abccxa - ",palindrome("abccxa"))
print("a - ",palindrome("a"))
print(" - ",palindrome(""))
