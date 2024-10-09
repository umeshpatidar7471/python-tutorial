# It can store elements of differnt types(int, float, string, etc.) # mutable[change]

"""marks = [94.4, 99.1, 77.1, 78.2, 90.5]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])"""

print()

# mix list
student = ["umesh", 21, 99.1, "mordi"]
print(student)
student[0] = "Nitesh"  # list are mutable(change)
print(student)

print()

# list slicing(similar to string)

score = [99, 100, 80, 70, 60]
print(score[0:4]) # [:4] same
print(score[0:])
print(score[-3:-1])

