marks = {
    "Andy": 88,
    "Amy": 66,
    "lists": [1, 2, 3, 4, 5],
    0 : "ANDY"
}
print(marks)
print(marks["Andy"])
print(marks["lists"])
print(marks[0])
print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.get("Andy"))
print(marks["Amy"])
marks.update({"Amy": 99})
print(marks)
marks.pop("Andy")
print(marks)
 #print(marks[aryan]) gives error
 #print(marks.get("aryan")) gives None
 # sets
s= {1, 2, 3, 4, 5 ,5 , "andy"}
s1 = {1, 2, 3, 4, 5,6,7,8}
print(s)
print(type(s))
s.add(6)
print(s)
e = set()
print(type(e))
print("union",s.union(s1))
print( "diffrence",s1.difference(s))
print("intersection",s.intersection(s1))
print(len(s))
s.remove(5)
print(s)