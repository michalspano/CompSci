textfile=open("Task1.txt", "w")
print("ASCII values of lower case alphabet:", file=textfile)
for i in range(97,123):
  print(chr(i) + " - " + str(i),file=textfile)
textfile.close()
