n=(input("Input: "))

def removeVowels(n):
  var=[]
  vowels="aAeEoOuUyYiI"
  for char in n:
    var.append(char)
  for x in vowels:
    for char in var:
      if char==x:
        var.remove(char)
  return var
output=removeVowels(n)
w=""
for letter in output:
  w+=letter
print(w)


