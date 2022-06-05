inputN=int(input("Input: "))
rangeN=inputN

def divisors(inputN):
  t=()
  for divisor in range(1,(rangeN+1)):
    if inputN % divisor == 0: #if remainder = 0; add this value to output 
      t+=(divisor,) #t = output
  return t
print(divisors(inputN))
