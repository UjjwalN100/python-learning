thisdict = {
  
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(type(thisdict))

car = {
  
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys() #Give us keys
print(x)

car["colors"] = "white"
print(x)

print(car)

y = car.values() #Give us values
print(y)

car["year"] = 2020
print(y)

#thisdict.pop("model")
del thisdict["model"]
print(thisdict)

for y in thisdict:
  print(thisdict[y])#Will give values of keys


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)
  
  for y in obj:
    print(y + ':', obj[y])