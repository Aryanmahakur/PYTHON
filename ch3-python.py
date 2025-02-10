name = "aryan"
#string slicing
nameshort = name[0:3]
#name[0:4] same as [0:]
charecter1 = name[1]
print(name[-4:-2])

print(charecter1)
print(nameshort)
#skip
num = "0123456789"
print(num[0:9:2])
print(num[1:9:2])
#lenght
givelength = "aryan"
print(len(givelength))
#endwidth
print(givelength.endswith("n"))
#startwith
print(givelength.startswith("a"))
#capitalize
print(givelength.capitalize())
print(givelength.upper())
print(givelength.replace("aryan","aryan mahakur"))
ex = "my name is \n \"aryan\""
print(ex)
#practice
inputname = input("enter your  name")
inputdate = input("enter the date")
print("good morning",inputname)
letter = '''Dear <|name|>,
Greetings from ABC coding house. I am happy to tell you about your selection.<|date|>'''
letter = letter.replace("<|name|>",inputname)
letter = letter.replace("<|date|>", inputdate)
print(inputname.find("  "))
print(letter)