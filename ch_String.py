#Multi-Line String
messsage = '''Hey, this is a message printed by me
Hope you will like it, Just
Trying to learn python
It's late i know but i will definitely do this.
'''
print(messsage)

#Accessing index of a string
a = "BhikaPatil"
print(a[1])

for x in "Banana":
   print(x)
   
#String length
print(len(a))   

#Check String

str1 = "This is my Python program"
if "Python" in str1:
  print("It is present")
  
#OR

print("Python" in str1)

print("Python" not in str1)

#Slicing
str2 = "Hello, World"
print(str2[2:5]) #here 5 is not included
print(str2[:5])
print(str2[2:]) #Slice to the end
print(str2[-5:-2])

#String Method
str3 = "ujjwal"

print(str3.upper()) #CAPITALIZE
print(str3.lower()) #lower

str4 = " Bhika Patil "
print(str4.strip()) #Cut the whitespaces

print(str3.replace("w", "l")) #Replaced
print(str2.split(","))

#String Concatnation
x = "Bhika"
y = "Patil"
z = x + ' ' + y
print(z)

#String Format we denote it by f
age = 21
print(f"My name is Bhika Patil and my age is {age}")

price = 21
txt1 = "Price is"
print(f"{txt1} {age}")

#OR

txt1 = f"Price is {price}"
print(txt1)