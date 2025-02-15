#q1
class BankAccount:
    def __init__(self, accountholder, balance):
        self.accountholder = accountholder
        self.balance = balance  
    def addmoney(self, money):
        self.balance += money
        print(f"Deposited: {money}, New Balance: {self.balance}")
    def withdraw(self,money):
        self.balance -=money
        print(f"withdraw: {money}, New Balance: {self.balance}")
john=BankAccount("john",5000)
john.addmoney(1000)
john.withdraw(500)

#q3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"name is {self.name} and age is {self.age}")

class Employee(Person):
     def __init__(self, name, age,salary):
         self.salary=salary
         super().__init__(name, age)

     def details(self):
         print(f"name is {self.name} and age is {self.age} and salary is {self.salary}")

# Example usage
p = Person("Aryan", 25)
p.details()

e = Employee("John", 30,9000)
e.details()
e.details
#q4
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def draw(self):
        # Loop through each row
        for i in range(self.length):
            # Loop through each column in the row
            for j in range(self.width):
                # Print '*' for each column, stay on the same line using end=""
                print('*', end="")
            # Move to the next line after each row
            print()

# Create a Rectangle with length 5 and width 10
rect = Rectangle(5, 5)

# Draw the rectangle using the draw method
rect.draw()


import random

# List of options
choices = ["rock", "paper", "scissors"]

# Randomly select one option
print(random.choice(choices))

userchoice=input("enter your choice")
print(userchoice)


