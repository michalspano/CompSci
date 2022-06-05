n=input("Input: ")

def removeVowels(n):
  var=""
  vowels="aAeEoOuUiIyY"
  for char in n:
    var+=char
  for x in vowels:
    for char in var:
      if char==x:
        var=var.replace(char, "")
  return var
print(removeVowels(n))
  
  
