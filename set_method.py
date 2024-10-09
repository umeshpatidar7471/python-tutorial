# add element in set
collection = set()

collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add("hello")
collection.add((1, 2, 3))  # only tuple add
print(len(collection))
print(collection)

print()

# remove the element in set
collection.remove("hello")
print(collection)
collection.remove((1, 2, 3))
print(collection)


print()

# empties the set
collection.clear()
print(len(collection))
print(collection)

print()

# removes an random value
collection1 = {"hello", "apna collage", 1, 2, 3}
print(collection1.pop())
print(collection1.pop())
print(collection1.pop())
print(collection1.pop())
print(collection1.pop())

print()

# combines both set values & return new
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1)
print(set2)

print()

# combines common values & returns new
print(set1.intersection(set2))
print(set1)
print(set2)

