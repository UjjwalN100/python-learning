#This is a list, surrounded by square brackets
l1 = ["Apple", "Banana", "Mango", "Orange", "Custardapple", "Cherry"]
print(l1)

#List can allow duplicate values too
l2 = ["Apple", "Mango", "Apple", "Orange", "Mango"]
print(l2)

#Length
print(len(l1))

#Datatype
print(type(l1))

#List Constructor
l3 = list(("apple", "banana", "orange", "cherry", "Watermelon"))
print(l3)

#Accessing List
print(l1[2])
print(l2[1:4])
print(l3[:3])
print(l1[-3:-1])
print(l2[1:])

#Changing item value
l3[3] = "blackcurrant"
print(l3)

#Changing in range
l3[1:2] = ["kiwi", "berry"] #Here it is adding berry in second index rather than replacing it.
print(l3)

l4 = ["Skoda", "Ferrari", "TATA", "Ford", "Suzuki"]
l4[1:3] = ["Lamborghini", "KIA"]
print(l4)

l5 = ["America", "India", "Italy", "Japan"]
l5[1:3] = ["Russia"]
print(l5)

#Insert
l6 = ["Avinash", "Mrunal", "Gajodhar", "Shilpa"]
l6.insert(0, "Avishkar") #It will not replace the item but will take its index
print(l6)

#Append
l6.append("Bhika")
print(l6)

#Extend is use to append another list
l6.extend(l5)
print(l6)

#You can also add any item other than list
l7 = ("Running", "Footaball", "Cricket")
l6.extend(l7)
print(l6)

#Remove
l6.remove("Bhika")
print(l6)

l8 = ["Samosa", "Pavwada", "Sandwich", "Vadapav", "Pizza"]
l8.pop(4)
print(l8)

#delete dos ame as pop
#del l8[0]
#print(l8)


#Clear method empties the list
l8.clear()
print(l8)

#For Loop in list
l9 = ["Potato", "Tomato", "Ladyfinger", "Brinjal"]

for x in l9:
  print(x)
  
#using range
for i in range (len(l9)):
  print(l9[i])
  
#while loop
i = 0
while i < len(l9):
  print(l9[i])
  i = i + 1

l10 = ["Urvesh", "Badkesh", "Ramesh", "Prajwal", "Bhujbal", "Kakasaheb", "Sandip", "Tanuja", "Aditi", "Rohini", "Rakesh", "Rupesh", "Rajesh", "Rinku"]

new_L10 = []

for x in l10:
  if "R" in x:
    new_L10.append(x)
print(new_L10)

#OR

new_L10 = [x for x  in l10 if "R" in x]
print(new_L10)

#Sorting
l10.sort()
print(l10)

#Reverse sorting
l10.sort(reverse = True)
print(l10)

#List copying
l10_Copy = l10.copy()
print(l10_Copy)