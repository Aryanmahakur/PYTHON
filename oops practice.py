class BankAccount:
    def __init__(self, accountholder="Blank", balance=0.0):
        self.accountholder = accountholder
        self.balance = balance

    def addmoney(self, money):
        self.balance += money
        print(f"Deposited: {money}, New Balance: {self.balance}")

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
            print(f"Withdrawn: {money}, Remaining Balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def display(self):
        print(f"Account Holder Name: {self.accountholder}")
        print(f"Account Balance: {self.balance}")

    @staticmethod
    def greet():
        print("Hello, welcome to our bank!")

# Creating an account
john = BankAccount("John", 500)

# Performing operations
john.addmoney(1000)
john.withdraw(500)
john.display()

# Calling static method
BankAccount.greet()

# inheritence
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name} is a good person and is {self.age} years old.")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def details(self):
        print(f"Name: {self.name} is a good person and is {self.age} years old. Salary: {self.salary}")

Employee1=Employee("Bob", 30, 70000)
Employee1.details()
#anothor question
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class College(Student):  # Inheriting from Student
    def __init__(self, name, age, course):
        super().__init__(name, age)  # Call parent constructor
        self.course = course  

    def details(self):
        super().details()  # Calling details method from the parent class (Student)
        print(f"Course: {self.course}")
   
# Creating an instance
student2 = College("John", 20, "Computer Science")

# Calling the overridden details method in College
student2.details()  # Correct method to call from College class

#ex3
class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school

    def details(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {self.school_name}")

# Creating instance
student1 = Student("John", 20)
student1.details()

# Using class method to change class attribute
Student.change_school("XYZ School")

# Calling the method again to see the updated class attribute
student1.details()

#property and getter and setter

class Student:
    def __init__(self, name, age):
        self._name = name  # Private attribute
        self._age = age    # Private attribute
    
    # Getter for the 'name' property
    @property
    def name(self):
        return self._name
    
    # Setter for the 'name' property
    @name.setter
    def name(self, value):
        self._name = value
    
    # Getter for the 'age' property
    @property
    def age(self):
        return self._age
    
    # Setter for the 'age' property
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age can't be negative!")
        else:
            self._age = value

# Create an instance of Student
student = Student("John", 20)

# Accessing properties
print(student.name)  # Calls the getter
print(student.age)   # Calls the getter

# Modifying properties using setter methods
student.name = "Jane"  # Calls the setter
student.age = 25       # Calls the setter

print(student.name)  # "Jane"
print(student.age)   # 25

# Trying to set a negative age (age can't be negative)
student.age = -5  # Prints "Age can't be negative!"



