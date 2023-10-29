# Take 2 inputs Name and Age and check person is Adult or Not
# name = input("Enter Your Name : ")
# age = input("Enter Your Age : ")
#
# print("\nIs Adult : ",int(age) >= 18)

# TYPE conversion : When we take input anything in python initial type is string only we want to typecast this into
# our required data type for further oprations
# old_age = input("Enter your Age : ")
# new_age = int(old_age)+10
# print("Age after 10 years = ",new_age)

# value convert into :
# float()
# str()
# bool()

# a = input("Enter first Number : ")
# b = input("Enter second number : ")
# sum = int(a) + int(b)
# print("The sum of 2 numbers : ", sum)


# String Function :

# name = "Omkar"
# name = name.upper()
# print(name)
# name = name.lower()
# print(name.find("kar"))  # checks the given char/substr in str and return index if present else return -1
# name = name.replace("kar", "car")  # use to replace any char/substr with new char/substr
# print(name)
# print("om" in name)  # We can search any char/substr but in keyword only returns the boolean value


# Arithmetic/comparison/Logical operations
# same as other programming language
# Logical Operator
# print((1>2)or(2>1))
# print((1>2)and(2>1))
# print(not(1>2))



# If-else Conditional ladder

# age = int(input("Enter Your age : "))
# if age>=18 and age<110:
#     print("Your are adult, You can Vote!")
# elif age<18 and age>12:
#     print("Your are in School, You can't Vote!")
# elif age>110:
#     print("Invalide Age Enter Again!")
# else:
#     print("You are child!!")







# Mini Calculator:

# a = float(input("Enter the first number : "))
# b = float(input("Enter the second number : "))
# operator = input("Enter the operator form [+,-,*,/,%,**] etc : ")
# if operator == "+":
#     print("Answer : ",a+b)
# elif operator == "-":
#     print("Answer : ",a-b)
# elif operator == "*":
#     print("Answer : ",a*b)
# elif operator == "/":
#     print("Answer : ",a/b)
# elif operator == "%":
#     print("Answer : ",a%b)
# elif operator == "**":
#     print("Answer : ",a**b)
# else:
#     print("Invalide Operator!!")




# Range

# numbers = range(5) #0,1,2,3,4 list
# print(numbers)


# Loops
# While Loop
# i = 1
# while i<=5:
#     print(i*"*")
#     i=i+1
#
#
# j=5
# while j>=1:
#     print(j*"*")
#     j=j-1


# For Loop
# for item in range(10):
#     print(item+1)


# List
# List can store any type of variable
#
# Marks = [87,98,96,'math']
# print(Marks)
# print(Marks[1:4]) #only prints elements on idex 1,2 & 3 excluding 4
#
# Marks.append(99) # use to add any elment in list from end of list
# print(Marks)
#
# Marks.insert(0,100) # use to insert any element at specific index
# print(Marks)
#
# print( 98 in Marks) #check is 98 is present in Marks list
#
# print("\nFor Loop : ")
# for i in range(len(Marks)):
#     print(Marks[i])
#
#
# print("\nWhile Loop : ")
# i=0
# while i<len(Marks):
#     print(Marks[i])
#     i=i+1
#
# Marks.pop(2)
# print(Marks)
#
# print("\nClear List")
# Marks.clear()
# print(Marks)






#Break & Continue

# student = ["Om","Ram","Raj","Soham","Jay"]
# This only prints student name up till Raj After that stop printing
# for stud in student:
#     print(stud)
#     if stud == "Raj":
#         break

# This print all student name except Raj
# for stud in student:
#     if stud=="Raj":
#         continue
#     print(stud)





# Tuple
# Same as List but it is Imutable means we cannot change the tuple data once we initialise them
# marks = 100,23,78,23,55,90 by default structure is tuple here we can declare or initialise them without brackets
# marks = (98,78,90,12,78,90,98,100,90)
# print("First 78 is at index : ",marks.index(78))
# print("90 repeats ",marks.count(90)," Times in Tuple ")




# Sets
# Same as tuple and list but here also one difference is that it only stores unique values inside it means duplicates not allowed here
# marks  = {98,78,80,80,78,70}
# marks1  = {98,70}
# print(marks)
# print(marks1.issubset(marks))




# Dictionary:
# Here we can save a data with key : value type
# marks = {"Om": 98,"Raj":95,"Jay":"87"}
# print(marks.keys())
# print(marks.values())



# Userdefine Function:
# def sum(first,second):
#     print(first +second)
#
# sum(10,20)