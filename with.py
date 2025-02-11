f = open("files.txt")
print(f.read())
f.close()
#smae can be written as
with open("files.txt") as f:
    print(f.read())