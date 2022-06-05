from random import *
textfile=open("Task2.txt", "w")
password=""
for i in range(8):
  password+=chr(randint(97,122))
print("Password: "+str(password),
      file=textfile)
textfile.close()
  
