i = 1
while i <= 10:
    mul = 2 * i  # Multiplication
    print( "2 *", i, "=", mul)   # Print the result
    i += 1       # Increment i
# print("End of the loop")
# for loop With STRINGS
lists = [1,"andy","amy",2,3,4,5]
i = 0
while i < len(lists):
    print(lists[i])
    i += 1  
    

# print("End of the loop")
#forloop with tuples
for l in range(1,10,2):
    if l == 5:
        print("l is 5")
        break
    print(l)
    for i in lists:
        print(i)
        print("End of the loop")
        #forloop with strings
        char = "aryan"
        for c in char:
            print(c)

    lists2 = [1,2,3,4,5,6,7,8,9,10]
    for l in lists2:
      print("l is",l)
    else:
        print("End of the loop")
        for a in range(10,20):
            if a == 15:
                continue
            print(a)
            for i in range(1,10):
                pass
            