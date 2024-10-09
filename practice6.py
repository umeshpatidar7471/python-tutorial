# print the length of a list.(list is the parameter)

cities = ["delhi", "mumbai", "pune", "goa", "chennai"]
heroes = ["thor", "ironman", "spiderman", "captain america", "antman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

print()

# print the elements of list in single line.(list is the parameter)

"""cities = ["delhi", "mumbai", "pune", "goa", "chennai"]
heroes = ["thor", "ironman", "spiderman", "captain america", "antman"]


def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)
print_list(cities)"""

print()

# find the factorial of n.(n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)  # one value
cal_fact(int(input("enter no:")))   # all of value


print()

# convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")


converter(1)