# Parent class
class Animal:
    def __init__(self, name, animal_type):  # Fixed parameter name
        self.name = name
        self.type = animal_type  # Store animal type

    def speak(self):
        return "Some sound"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Bark"

# Child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return "Meow"

# Creating objects
dog = Dog("Buddy", "Dog")  # Passing both required arguments
cat = Cat("Whiskers", "Cat")  # Fixed: Added missing second argument

print(f"{dog.name} ({dog.type}) says {dog.speak()}")
print(f"{cat.name} ({cat.type}) says {cat.speak()}")
 #ex2class Person:
 # Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name} is a good person and is {self.age} years old.")

# Child class inheriting from Person
class Employee1(Person):
    def __init__(self, name, age, job_title, salary):
        # Calling parent class constructor using super()
        super().__init__(name, age)
        self.job_title = job_title
        self.salary = salary

    # Overriding the details method
    def details(self):
        super().details()  # Calling parent class method
        print(f"Works as {self.job_title} with a salary of {self.salary}.")

# Creating objects
person1 = Person("Alice", 23)
employee1 = Employee1("Bob", 30, "Software Engineer", 70000)

# Calling the methods
person1.details()
person1.details()
print()
employee1.details()  # Calls overridden method
#ex3

# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Names: {self.name}, Age: {self.age}")

# Child class inheriting from Person
class Employee(Person):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)
        #self.name = name
        #self.age = age
        self.job_title = job_title
        self.salary = salary

    def details(self):
        super().details()  # Calling the parent class method
        print(f"Job Title: {self.job_title}, Salary: {self.salary}")

# Creating an object of Employee class
employee = Employee("Alice", 28, "Software Developer", 80000)

# Calling the details method
employee.details()
#ex4
class Employee5:
    a = 10  # Class variable

    @classmethod
    def show(cls):
        print(cls.a)  # Accessing class variable using cls
        
        
  


# Alternatively, calling via an instance (not recommended for class methods)
p = Employee5()
p.a = 20  # Instance variable

p.show()
#ex5
class Employee:
    def __init__(self, name, salaryy):
        self._name = name        # Private attribute (by convention)
        self._salary = salaryy   # Private attribute (by convention)

    @property
    def salary(self):
        """Getter method for salary"""
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        """Setter method for salary"""
        if new_salary < 0:
            print("Salary cannot be negative!")
        else:
            self._salary = new_salary

# Creating an Employee object
emp = Employee("Alice", 50000)

# Using property getter
print(emp.salary)  # Accessing salary like an attribute

# Using property setter
emp.salary = 60000  # Modifying salary
print(emp.salary)

# Trying to set a negative salary
emp.salary = -5000  # Will show an error message
#ex6
class Number:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a # Returning a new Number object

# Creating objects
a = Number(5)
b = Number(6)

print(a + b)


