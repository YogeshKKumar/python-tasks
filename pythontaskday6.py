# Task 1: Encapsulation

class User:
    def __init__(self):
        self.__user_name = ""
        self.__pwd = ""

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")


u = User()
u.set_user("john", "1234")
u.register()
u.login()


# Task 2: Inheritance

class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


s = Student()
s.register()
s.login()
s.student_greet()

f = Faculty()
f.register()
f.login()
f.faculty_greet()

t = TempFaculty()
t.register()
t.login()
t.tempFaculty_greet()


# Task 3: Method Overriding

class User:
    def greet(self):
        print("Welcome User")


class Student(User):
    def greet(self):
        print("Welcome Student")


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")


student = Student()
faculty = Faculty()

student.greet()
faculty.greet()


# Task 4: Method Chaining

class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


user = User()
user.login().greet().register()


# Task 5: Combined Task (Real-Time)

class User:
    users_count = 0

    def __init__(self, name):
        self.__name = name
        User.users_count += 1

    def login(self):
        print(f"{self.__name} logged in")
        return self

    def greet(self):
        print("Welcome User")
        return self

    def register(self):
        print(f"{self.__name} registered")
        return self


class Student(User):
    def greet(self):
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self


u1 = Student("John")
u1.login().greet().register()

u2 = Faculty("Alice")
u2.login().greet().register()

print("Total Users:", User.users_count)