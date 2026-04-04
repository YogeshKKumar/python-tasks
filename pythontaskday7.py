# Task 1: Use super() properly

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration


# Task 2: Apply Abstraction

from abc import ABC, abstractmethod

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


class Student(AbstractUser):
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"{self.name}, {self.id}, {self.dept}, {self.fees}"


class Faculty(AbstractUser):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def get_details(self):
        return f"{self.name}, {self.id}, {self.salary}"


# Task 3: Sorting using key

students = [
    Student("John", 1, "CSE", 60000),
    Student("Meena", 2, "IT", 45000)
]

faculty = [
    Faculty("Alice", 101, 40000),
    Faculty("Bob", 102, 25000)
]

students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)


# Task 4: Use map()

names = list(map(lambda s: s.name, students))
print(names)


# Task 5: Use filter()

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))


# Task 6: Use reduce()

from functools import reduce

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("Total Fees:", total_fees)
print("Total Salary:", total_salary)


# Task 7: Higher Order Function

def process_users(users, func):
    return list(map(func, users))

print(process_users(students, lambda s: s.name))


# Final Challenge

students = [
    Student("John", 1, "CSE", 60000),
    Student("Meena", 2, "IT", 45000),
    Student("Arun", 3, "ECE", 70000)
]

faculty = [
    Faculty("Alice", 101, 40000),
    Faculty("Bob", 102, 25000),
    Faculty("David", 103, 50000)
]

# Print all details
for s in students:
    print(s.get_details())

for f in faculty:
    print(f.get_details())

# Sorted data
students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)

# Filtered data
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

# Totals
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("High Fee Students:", [s.name for s in high_fee_students])
print("High Salary Faculty:", [f.name for f in high_salary_faculty])
print("Total Fees:", total_fees)
print("Total Salary:", total_salary)