# odd or even
num = int(input("Enter number:"))

if(num % 2 == 0):
    print("even")
else:
    print("odd")

print()

# greatest number
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if(a >= b and a >= c):
    print("first number is largest",a)
elif(b >= c):
    print("second is largest:",b)
else:
    print("third is largest:",c)

print()

"""x = int(input("Multiple value:"))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not multiple of 7")"""

print()

"""A = 5  &  G = M
A = 2  &  G = F"""

"""A = int(input("A :"))
G = input("M/F :")

if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 and G =="M"):
    print("fee is 300")
else:
    print("no fee")"""
