class Employees:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

# Creating an instance of Employees
Aryan = Employees("Aryan", 23, 10000)


# Printing attributes
print(Aryan.name)  # Output: Aryan
print(Aryan.age)   # Output: 23
print(Aryan.salary) # Output: 10000

class City:
    nameofcity = "Delhi"
    population = "1.5 m" #class attribute
    def getinfo(example):
        print("The city of", example.nameofcity, "has a population of", example.population)

    @staticmethod
    def greet():
      print("Hello mumbai")
# Creating an instance of City
delhi = City()
delhi.nameofcity = "Delhi"
mumbai = City()
mumbai.nameofcity = "Mumbai" #object attribute instance attribute
mumbai.greet()

# Printing the attribute
print(delhi.nameofcity,delhi.population)  # Output: Delhi
print(mumbai.nameofcity,mumbai.population)  # Output: Delhi
City.getinfo(delhi) # or delhi.getinfo()
#static method


