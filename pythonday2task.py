# Bitwise Operator Tasks

a = 10
b = 6
print(a & b)

x = 12
y = 5
print(x | y)

num = 8
print(~num)

a = 15
b = 9
print(a ^ b)

num = 7
print(num << 2)

num = 20
print(num >> 1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a & b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a ^ b)


# String Tasks

s = "hi"
print(s * 4)

s = "python"
print(s * 3)

a = "super"
b = "man"
print(a + b)

a = "hello"
b = " "
c = "world"
print(a + b + c)

name = input("Enter name: ")
print(name * 5)

a = input("Enter first string: ")
b = input("Enter second string: ")
print(a + b)


# Input & Type Casting Tasks

name = input("Enter name: ")
print(type(name))

age = int(input("Enter age: "))
print(age)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

m1 = int(input("Enter mark1: "))
m2 = int(input("Enter mark2: "))
print((m1 + m2) / 2)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(3 * a * 2 + b - 2)

num = input("Enter number: ")
print(type(num))
num = int(num)
print(type(num))


# Unit Digit Tasks

num = input("Enter number: ")
print(num[-1])

num = int(input("Enter number: "))
print(num % 10)

num = int(input("Enter number: "))
print(num // 10)

num = int(input("Enter number: "))
print((num // 10) % 10)

num = int(input("Enter 5 digit number: "))
print(num % 10)


# If Statement Tasks

if 10 >= 5:
    print("10 is greater than or equal to 5")

num = int(input("Enter number: "))
if num > 50:
    print("Greater than 50")

age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")

num = int(input("Enter number: "))
if num > 100:
    print("Greater than 100")

num = int(input("Enter number: "))
if num >= 0:
    print("Non-negative number")


# If-Else Tasks

num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

marks = int(input("Enter marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")

num = int(input("Enter number: "))
if num >= 0:
    print("Positive")
else:
    print("Negative")

num = int(input("Enter number: "))
if num > 10:
    print("Greater than 10")
else:
    print("Not greater than 10")


# Nested If Tasks

age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Rejected")
else:
    print("Rejected")

age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")


# Match Statement Tasks

day = int(input("Enter number (1-7): "))match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

num = int(input("Enter number (1-3): "))match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")

num = int(input("Enter number (1-4): "))match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")