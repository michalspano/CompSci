s="Write a message to store:"
sentence=input(s)

if sentence=="delete":
  textfile=open("messages.txt","w")
  textfile.close()
elif sentence=="":
  pass
else:
  textfile=open("messages.txt", "a")
  textfile.write(sentence + "\n")
  textfile.close()
