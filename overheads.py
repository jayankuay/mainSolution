from pathlib import Path
import matplotlib.pyplot as plt
import csv

fp = Path.cwd/"Overheads.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    salary_expense = []
    interest_expense = []
    marketing_expense = []
    rental_expense = []
    overflow_expense = []
    penalty_expense = []
    depreciation_expense = []
    maintenance_expense = []
    shipping_expense = []
    human_resource_expense = []

    for row in reader:
        if row[1] == "Salary Expense":
            salary_expense.append(row[2])
        elif row[1] == "Interest Expense":
            interest_expense.append(row[2])
        elif row[1] == "Marketing Expense":
            marketing_expense.append(row[2])
        elif row[1] == "Rental Expense":
            rental_expense.append(row[2])
        elif row[1] == "Overflow Expense":
            overflow_expense.append(row[2])
        elif row[1] == "Penalty Expense":
            penalty_expense.append(row[2])
        elif row[1] == "Depreciation Expense":
            depreciation_expense.append(row[2])
        elif row[1] == "Maintenance Expense":
            maintenance_expense.append(row[2])
        elif row[1] == "Shipping Expense":
            shipping_expense.append(row[2])
        elif row[1] == "Human Resource Expense":
            human_resource_expense.append(row[2])