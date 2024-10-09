# print even numbers using range() & for loop

for i in range(2, 100, 2):
    print(i)

print()

# print odd numbers using range() & for loop

for i in range(1, 100, 2):
    print(i)

print()

# print numbers from 1 to 100

for i in range(1, 101):
    print(i)

print()

# print numbers from 100 to 1

for i in range(100, 0, -1):
    print(i)

print()

# print the multiplication table of a number n

n = int(input("enter number:"))

for i in range(1, 11):
    print(n * i)

print()

# find the sum of first natural number.(using for loop & while loop)

# for loop
n = 5   # sum = 1+2+3+4+5

sum = 0
for i in range(1, n+1):
    sum += i

print("total sum =", sum)

print()

# while loop
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum =", sum)

print()

# find the factorial of first n numbers(using for loop & while loop)

# for loop
n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print("factorial =", fact)

print()

# while loop
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =", fact)