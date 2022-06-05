def splitname(fullname):
  position=fullname.find(" ")
  name=fullname[:position]
  surname=fullname[position+1:]
  return name, surname
info=splitname("Michal Spano")
for i in info:
  print(i)


