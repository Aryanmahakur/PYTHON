#walrus
if(n := len([1, 2, 3])) > 2:
    print(f"List is too long ({n} elements, expected <= 2)")
    
#type
n : int = 5
name : str = "Alice"
def sum(a: int, b: int) -> int:
    return a + b
print(sum(5, 10))  # Output: 15
#importing
from typing import List, Tuple , Dict, Any, Union
numbers: List[int] = [1, 2, 3, 4, 5]
person: Tuple[str, int] = ("Alice", 25)
scrores : Dict[str, int] = {"Math": 90, "Science": 80}
identifier: Union[int, str] = 5

print(numbers)  # [1, 2, 3, 4, 5]
print(person)  # ('Alice', 25)
print(scrores)  # {'Math': 90, 'Science': 80}
print(identifier)  # 5
#match
def http_status(status):
    match status:
        case 200:
            print("OK")
        case 400:
           return "Bad Request"
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case _:
            print("Unknown Status")

print(http_status(200))  # Output: OK
print(http_status(400))  # Output: Bad Request
#dictionary
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)  # Merges dict2 into dict1
print(dict1)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2  # Merges dict1 and dict2
print(merged_dict)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}  # Merges dict1 and dict2
print(merged_dict)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#exception
try:
    a = int(input("Enter a number: "))  # Try to convert input to an integer
    print(a)  # Print the entered number if successful
except ValueError:
    print("Invalid input! Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")  # Print the error message if an exception occurs

#raising exception
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if b == 0:
    raise ZeroDivisionError("Division by zero is not allowed")
else:
    print(f"{a} / {b} = {a / b}")
print( "division of a and b is",a / b)
#try else
try:
    a = int(input("Enter a number: "))  # Convert input to an integer
    b = int(input("Enter another number: "))
    print(f"{a} / {b} = {a / b}")  # Perform the division if no error occurs
except Exception as e:  # Catch any exception
    print(f"An error occurred: {e}")
else:
    print("Division was successful")  # This will run only if no exceptions occur
#try finally
try:
    a = int(input("Enter a number: "))  # Convert input to an integer
    b = int(input("Enter another number: "))
    print(f"{a} / {b} = {a / b}")  # Perform the division if no error occurs
except Exception as e:  # Catch any exception
    print(f"An error occurred: {e}")
else:
    print("Division was successful") 
finally:
    print("Exiting...") # This will always run
    # main
from module import myfunc
if __name__ == "__main__":
print("we are directly running the file")
myfunc()
print(__name__)  
