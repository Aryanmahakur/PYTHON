#pip freeze show all the installed packages
#lamda function is a small anonymous function
from functools import reduce
def square(x):
    return x*x

print(square(5))
square = lambda x: x*x
print(square(5))
#join method is used to join strings
i= ['a', 'b', 'c', 'd']
final = "-".join(i)
print("-".join(i))
#format method
name = "John"
age = 23
print(f"{name} is {age} years old")
print("{0} is {1} years old".format(name, age))
 
 #map
l = [1, 2, 3, 4, 5]
squared = lambda x: x * x  # ✅ Correctly defining lambda function

sqlist = map(squared, l)  # ✅ Correct usage of map()
print(list(sqlist))  # Output: [1, 4, 9, 16, 25]
#filter
def even(x):
    if (x%2 == 0):
        return True
    else:
        return False
    
l = [1, 2, 3, 4, 5]
evennumbers = filter(even, l)
print(list(evennumbers))

#reduce
def sum(x,y):
    return x + y
mul = lambda x,y: x*y
print(reduce(mul, l) ) # Output: 120
print(reduce(sum,l) ) # Output: 15
