set1 = {"apple", "banana", "cherry", "litchie"}

print(set1)
print(type(set1))

for x in set1:
  print(x) #We can access items of the set by using for loops but not by accessing it thorugh index numbers as we were using in tuple and list
  
print("banana" in set1)

#Adding item in set
set1.add("orange")
print(set1)

#Adding two sets
set2 = {"guava", "berry", "mango", "watermelon"}

set1.update(set2)
print(set1)

#Join a set (Operator for union = |)
set3 = set1.union(set2)
print(set3)

#OR

set3 = set1 | set2
print(set3)

#Join a set and tuple
x = ("bmw", "kia", "tata", "MG")

y = set1.union(x)
print(type(y))