f = open("files.txt" , "r")
data = f.read()

print(data)
f.close()


st = "hello how are you"
f = open("filess.txt","w")
f.write(st)
f.close()
# Open the file in read mode
f = open("files.txt", "r")

# Read the first line
line = f.readline()

# Use while loop to print data line by line
while line:
    print("printing line by line")
    print(line.strip())  # Using strip() to remove extra newlines
    line = f.readline()  # Read the next line

# Close the file
f.close()


