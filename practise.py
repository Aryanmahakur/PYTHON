'''
#ch1

#ch2

#ch3
name = "aryan"
sl=name[0:3]
print(sl)
word ="amazing"
print(len(word))
print(word.endswith("ing"))
print(word.startswith("m"))
print(word.count("a"))
print(word.find("a"))
print(word.index("a"))
print(word.capitalize())
print(word.replace("a","z"))
print(word[:7])
print(word[0:])
print(word[0:7:2])

#ch4
#list
l = [1, 2, 3, 4, 5]
print(l)
print(l[0])
l[0] = 6
print(l)
l.append(7)
print(l)
l.insert(1, 8)
print(l)
l.remove(8)
print(l)
l.pop(3)
print(l)
l.sort()
print( "shorting ",l)
l.reverse()
print(l)
l.clear()
print(l)

#tuple
t = (1, 2, 3, 4, 5)
print(t)
print(t[0])
#t[0] = 6 #TypeError: 'tuple' object does not support item assignment
print(t.count(1))
print(t.index(1))

#dictionary
d = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(d)
print(d["key1"])
d["key1"] = "value4"
print(d)
print(d.items())
print(d.keys())
print(d.values())
print(d.update({"key5": "value5"}) )
print(d)
print(d.pop("key5"))
print(d)
print(d.get("key1"))
print(d)

#sets
s = {1, 2, 3, 4, 5}
s.add(6)
print(s)
s.update([7, 8, 9])
print(s)

print(len(s))
s.remove(9)
print(s)
s.discard(8)
print(s)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1.union(s2))
print("union")
print(s1.intersection(s2))
print("intersection")
print(s1.difference(s2))

#ch5
a= 5


if  a<10 :
    print("a is less than 10")
else:
    print("a is greater than 10")

ip = int(input("enter the number"))

if ip%2==0:
    print("even")
else:
    print("odd")

age = int(input("enter the age"))
if age<18:
    print("not eligible")

elif age>18:
    print("eligible")
else:
    print("error")

    
    #ch6
i=0
while i<10:
    print(i)
    i+=1

l=[1,2,3,4,5]
for i in l:
    print(i)
'''
#ch8
def func1():
    print("hello")

func1()


def func2(name):
    gr = "Good Morning " + name
    return gr

a = func2("Aryan")
print(a)
def greet(name, ending="Good Morning"):
    print(f"{ending} {name}")

a = greet("Aryan" , "Good Night")
print(a)

#ch10

class City:
    def getinfo(self):
        print("The city of", self.nameofcity, "has a population of", self.population)

delhi = City()
delhi.nameofcity = "Delhi"
delhi.population = "1.5 m"

City.getinfo(delhi)  # Calling the method

#ch10
class Employees:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

@staticmethod
def greet(name):
    print("Hello Aryan")
# Creating an object of Employees class
aryan = Employees("Aryan", 23, 10000)
a=greet("Aryan")
print(a)
# Printing object attributes
print(aryan.name)
print(aryan.age)    
print(aryan.salary)

    #questions
 #1
'''
num = [1, 2, 3, 4, 5, 6, 7, 8]

index = 0
while index < len(num):
    if num[index] % 2 != 0:
        print( "odd" , num[index])
    index += 1
    #2
num = int(input("enter number"))
if(num%2==0):
    print("number is even" , num)
else:
        print("odd")
        
    
    
#3
num = [10, 45, 78, 23]
max_value = num[0]  # Assume the first element is the largest
index = 1  # Start from the second element

while index < len(num):
    if num[index] > max_value:
        max_value = num[index]  # Update max_value if a larger number is found
    index += 1

print("The biggest number is:", max_value)
'''



       
