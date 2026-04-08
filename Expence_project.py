# Smart Expense Management System

import mysql.connector
from abc import ABC, abstractmethod
from functools import reduce
from datetime import datetime


# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="expense_db"
)
cursor = conn.cursor()


# Abstract Class
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# User Class
class User(AbstractUser):
    def __init__(self, name):
        self.__name = name

    def add_user(self):
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (self.__name,))
        conn.commit()

    def get_details(self):
        return self.__name


# Expense Class (Inheritance)
class Expense(User):
    def __init__(self, name, user_id, amount, category, description, date):
        super().__init__(name)
        self.__user_id = user_id
        self.__amount = amount
        self.__category = category
        self.__description = description
        self.__date = date

    def add_expense(self):
        query = """INSERT INTO expenses 
        (user_id, amount, category, description, date)
        VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (self.__user_id, self.__amount,
                               self.__category, self.__description, self.__date))
        conn.commit()

    def get_details(self):
        return f"{self.__amount}, {self.__category}, {self.__description}, {self.__date}"


# View Expenses (JOIN)
def view_expenses(user_id):
    query = """
    SELECT users.name, expenses.amount, expenses.category, expenses.description, expenses.date
    FROM expenses
    JOIN users ON users.user_id = expenses.user_id
    WHERE users.user_id = %s
    """
    cursor.execute(query, (user_id,))
    return cursor.fetchall()


# Filter Expenses
def filter_by_category(expenses, category):
    return list(filter(lambda x: x[2] == category, expenses))


def filter_by_date(expenses, date):
    return [e for e in expenses if str(e[4]) == date]


# Total Expense
def total_expense(expenses):
    amounts = list(map(lambda x: x[1], expenses))
    return reduce(lambda a, b: a + b, amounts, 0)


# Category-wise Spending
def category_spending(expenses):
    categories = {e[2] for e in expenses}
    return {c: sum(e[1] for e in expenses if e[2] == c) for c in categories}


# Monthly Report
def monthly_report(expenses):
    report = {}
    for e in expenses:
        month = str(e[4])[:7]
        report[month] = report.get(month, 0) + e[1]
    return report


# Highest Expense
def highest_expense(expenses):
    return reduce(lambda a, b: a if a[1] > b[1] else b, expenses)


# Smart Insight
def smart_insight(expenses):
    cat_spend = category_spending(expenses)
    if not cat_spend:
        return "No data"
    max_cat = max(cat_spend, key=cat_spend.get)
    return f"You are spending too much on {max_cat}"


# Update Expense
def update_expense(exp_id, amount):
    cursor.execute("UPDATE expenses SET amount=%s WHERE exp_id=%s", (amount, exp_id))
    conn.commit()


# Delete Expense
def delete_expense(exp_id):
    cursor.execute("DELETE FROM expenses WHERE exp_id=%s", (exp_id,))
    conn.commit()


# Sample Flow

# Add user
# u = User("Ravi")
# u.add_user()

# Add expense
# e = Expense("Ravi", 1, 500, "Food", "Lunch", "2025-03-01")
# e.add_expense()

# View & Analyze
# data = view_expenses(1)
# print(data)

# print(filter_by_category(data, "Food"))
# print(filter_by_date(data, "2025-03-01"))
# print(total_expense(data))
# print(category_spending(data))
# print(monthly_report(data))
# print(highest_expense(data))
# print(smart_insight(data))
