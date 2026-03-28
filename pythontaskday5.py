# Task 1: User Info Manager 

def create_user(name, age, role):
    return {"name": name.title(), "age": age, "role": role}

users = []

users.append(create_user("ravi", 22, "developer"))
users.append(create_user("meena", 21, "analyst"))

for user in users:
    print(user)


# Task 2: Dynamic Calculator

def calculate_total(*numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

print(calculate_total(10, 20, 30, 40))


# Task 3: Keyword Config System 

def system_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0")


# Task 4: Factorial Service 

def factorial(n):
    if n < 0:
        return "Error: Negative number"
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# Task 5: Memory Optimization

def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

gen = square_generator(5)
lst = [i * i for i in range(1, 6)]

print(type(gen))
print(type(lst))

for val in gen:
    print(val)


# Task 6: Exception Handling Module

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Program Completed")


# Task 7: File Handling

file = open("team_data.txt", "w")
file.write("Ravi, 22, Developer\n")
file.write("Meena, 21, Analyst\n")
file.close()

file = open("team_data.txt", "r")
content = file.read()
print(content)
print("File closed:", file.closed)
file.close()