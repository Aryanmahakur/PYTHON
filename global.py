a=20
def fun():
   # global a
    a=10
    print(a)

fun()
print(a)
#emurate
l= [1, 2, 3, 4, 5]
index = 0
for i in l:
    print(f"Index: {index}, Value: {i}")
    index += 1
    # this can be simpler using enumerate
for index, value in enumerate(l):
    print(f"Index: {index}, Value: {value}")
    #list comprehension
mylist = [1, 2, 3, 4, 5]
squared = []
for item in mylist :
    squared.append(item ** 2)
print(squared)
#or
squaredlist = [i*i for i in mylist]
print(squaredlist)