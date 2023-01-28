myFile = open("newFile.txt", "r")
line = myFile.read()

print(line)

for line in myFile:
    print(line, end="")