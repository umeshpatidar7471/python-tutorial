# print the elements of followmg list using a for loop:

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums:
    print(el)

print()

# Search for a number x in this tuple using for loop:

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 49]

x = 49
idx = 0
for el in nums:
    if(el == x):
        print("number found at idx:", idx)
    idx += 1