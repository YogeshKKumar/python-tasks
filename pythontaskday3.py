# Section 1: Loop Basics (1–10)

# Print numbers from 1 to 50 using for loop
for i in range(1, 51):
    print(i)

# Print even numbers from 1 to 100
for i in range(2, 101, 2):
    print(i)

# Print odd numbers from 1 to 100
for i in range(1, 101, 2):
    print(i)

# Print multiplication table of 7
for i in range(1, 11):
    print(7 * i)

# Find sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(total)

# Print numbers in reverse from 50 to 1
for i in range(50, 0, -1):
    print(i)

# Count how many numbers are divisible by 3 (1–100)
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print(count)

# Print squares of numbers from 1 to 10
for i in range(1, 11):
    print(i * i)

# Print cube of first 10 numbers
for i in range(1, 11):
    print(i ** 3)

# Take input n, print numbers from 1 to n
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i)


# Section 2: While Loop (11–15)

# Print numbers from 1 to 20 using while
i = 1
while i <= 20:
    print(i)
    i += 1

# Find factorial of a number using while
n = int(input("Enter number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)

# Reverse a number using while
num = int(input("Enter number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(rev)

# Count digits in a number
num = int(input("Enter number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)

# Keep asking input until user enters "stop"
while True:
    text = input("Enter something: ")
    if text == "stop":
        break


# Section 3: Nested Loop (16–20)

# Print pattern *
for i in range(1, 5):
    print("*" * i)

# Print pattern 1,12,123,1234
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Print multiplication table (1 to 5)
for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()

# Print A B C pattern
for i in range(3):
    for j in ['A', 'B', 'C']:
        print(j, end=" ")
    print()

# Print 1 to 9 matrix
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()


# Section 4: String Basics (21–25)

# Count total characters in a string
s = input("Enter string: ")
print(len(s))

# Count vowels in a string
count = 0
for ch in s:
    if ch.lower() in "aeiou":
        count += 1
print(count)

# Count consonants in a string
count = 0
for ch in s:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1
print(count)

# Reverse a string using loop
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# Check if string is palindrome
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Section 5: String Slicing (26–30)

# Print first 5 characters of a string
print(s[:5])

# Print last 3 characters
print(s[-3:])

# Print string in reverse using slicing
print(s[::-1])

# Print every 2nd character
print(s[::2])

# Remove first and last character
print(s[1:-1])


# Section 6: List Basics (31–35)

# Create a list of 5 numbers and print sum
lst = [1, 2, 3, 4, 5]
print(sum(lst))

# Find maximum value in list
print(max(lst))

# Find minimum value in list
print(min(lst))

# Count total elements in list
print(len(lst))

# Check if element exists in list
x = int(input("Enter element: "))
print(x in lst)


# Section 7: List Operations (36–40)

# Add 3 elements using append()
lst = []
lst.append(1)
lst.append(2)
lst.append(3)
print(lst)

# Insert element at specific index
lst.insert(1, 10)
print(lst)

# Remove element using remove()
lst.remove(2)
print(lst)

# Reverse list without using .reverse()
rev = []
for i in lst:
    rev = [i] + rev
print(rev)

# Sort list without using .sort()
lst = [5, 2, 8, 1, 3]
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)