file=open("documents.txt","r")
directory=open("file.html","w")

n=""
for line in file:
  n=(line.strip())
  directory.write('<a href='+n+'>')
  directory.write("<p>"+line+"</p>")
  directory.write("</a>")
directory.close()
