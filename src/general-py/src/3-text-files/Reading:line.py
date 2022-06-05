textfile=open("info1.txt", "r")

line_count=0
lines=()
for line in textfile:
  line_count+=1
  lines=lines+(line.strip(),)
textfile.close()

print("Number of lines: " + str(line_count))
n=int(input("Line to be displayed: "))
print(repr(lines[n-1]))
