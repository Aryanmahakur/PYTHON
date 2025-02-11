def avg():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    average=(a+b)/2
    print("The average of the two numbers is", average)
avg()
def greet():
    g = input("Enter your name: ")
    print("Hello", g)
greet()
#function with arguements
def greet(name,ending):
    print("Hello", name)
    print(ending)
    return "ok"
   
a=greet("Aryan","thanks")
print(a)

def gooday(name,ending="Good Morning"):
    print(f"{ending} {name}")
gooday("Aryan","Good Night")
gooday("Arman")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
