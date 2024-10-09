"""key:value pairs
unordered,mutable & don,t allow duplicate keys"""

dict = {
    "key" : "value",
    "name" : "Umesh",
    "cgpa" : 9.6,
    "subjects" : ("python", "java", "html"),
    "marks" : [98, 99, 88],
}
print(dict)
print(type(dict))
print(dict["name"])
print(dict["subjects"])
dict["name"] = "kajal"
dict["surname"] = "patidar"
print(dict)

print()

# Nested dictionary
"""student = {
    "name" : "umesh",
    "score" : {
        "chem": 98,
        "phy": 94,
        "math": 95,
    }
}

print(student)
print(student["score"])
print(student ["score"]["chem"])"""