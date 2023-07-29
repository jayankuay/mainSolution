from pathlib import Path
import matplotlib.pyplot as plt
import csv

fp = Path.cwd()/"Overheads.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    overheads = []

    for row in reader:
        overheads.append(row)
        

def highest_overhead_expense(expense):
    """
    Will find the highest overhead expense incurred over 90 day period of running the business
    """

    highest_expense = 0
    highest_overhead = 0
    for value in expense:
        overhead = float([value][1])
        if overhead > highest_overhead:
                highest_overhead = overhead
                highest_expense = value[0]

    return [highest_expense, highest_overhead]

highest_overhead_report = highest_overhead_expense('Overheads.csv')   

file_path = Path.cwd()/"summary_report.txt"
file_path.touch()

with file_path.open(mode = "w", encoding = "UTF-8") as file:
    file.write(f"[HIGHEST OVERHEAD] {highest_overhead_report[0]}: {highest_overhead_report[1]}%")
# Ignore the below codes thanks
#    salary_expense = []
#    interest_expense = []
#    marketing_expense = []
#    rental_expense = []
#    overflow_expense = []
#    penalty_expense = []
#    depreciation_expense = []
#    maintenance_expense = []
#    shipping_expense = []
#    human_resource_expense = []

#    for row in reader:
#        if row[1] == "Salary Expense":
#           salary_expense.append(row[2])
#        elif row[1] == "Interest Expense":
#            interest_expense.append(row[2])
#        elif row[1] == "Marketing Expense":
#            marketing_expense.append(row[2])
#        elif row[1] == "Rental Expense":
#            rental_expense.append(row[2])
#        elif row[1] == "Overflow Expense":
#            overflow_expense.append(row[2])
#        elif row[1] == "Penalty Expense":
#            penalty_expense.append(row[2])
#        elif row[1] == "Depreciation Expense":
#            depreciation_expense.append(row[2])
#        elif row[1] == "Maintenance Expense":
#            maintenance_expense.append(row[2])
#        elif row[1] == "Shipping Expense":
#            shipping_expense.append(row[2])
#        elif row[1] == "Human Resource Expense":
#            human_resource_expense.append(row[2])

