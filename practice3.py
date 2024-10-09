# print numbers from 1 to 100

"""i = 1
while i <= 100:  # stopping condition
    print(i)
    i += 1"""

print()

# print numbers from 100 to 1

"""i = 100
while i >= 1:
    print(i)
    i -= 1"""

print()

# print the multiplication table of number n

n = int(input("Enter number :"))  # n = any no.
i = 1
while i <= 10:
    print(n*i)
    i += 1

print()

"""print the elements of following list using a loop
   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"""

nums = [1, 4, 9,16, 25, 36, 49, 64, 81, 100]

i = 0
while i < len(nums):
    print(nums[i])
    i += 1

print()

# print the string following list using a loop

heroes = ["batman","ironman","spiderman","superman"]

i = 0
while i < len(heroes):
     print(heroes[i])
     i += 1

print()

# Search for a number x in this tuple using loop

num = (2, 4, 6, 8, 10, 2, 4, 6)

x = int(input("enter no:"))

i = 0
while i < len(num):
    if(num[i] == x):
        print("found at idx", i)
    else:
        print("finding...")
    i += 1

print()

# Break & Continue keyword using in any loop

"""num = (2, 4, 6, 8, 10, 2, 4, 6)

x = int(input("enter no:"))

i = 0
while i < len(num):
    if(num[i] == x):
        print("found at idx", i)
        break      # exit the loop & not search again 
    else:
        print("finding...")
    i += 1

print()

i = 0
while i <= 10:
    if(i % 2 == 0): # odd number
     # if(i % 2 != 0):  # even number
        i += 1
        continue   # skip
    print(i)
    i += 1"""