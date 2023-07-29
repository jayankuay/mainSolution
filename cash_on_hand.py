from pathlib import Path
import matplotlib.pyplot as plt
import csv

def cash_difference(file):
    """
    - TO calculate the difference in cash on hand
    """
    total_difference = 0
    #difference = 0
    #total_difference_list = 0
    cash_on_hand = 0
    previous_cash_on_hand = 0
    surplus_day = 0
    highest_surplus = 0
    fp = Path.cwd()/"Cash on Hand.csv"
    with fp.open(mode="r",encoding="UTF-8",newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cash_on_hand = float(row[1])
            previous_cash_on_hand = 0
            #total_difference = previous_cash_on_hand - following_cash_on_hand
            if previous_cash_on_hand > 0:
            #if cash_on_hand > total_difference:
                total_difference = cash_on_hand - previous_cash_on_hand
                if total_difference > highest_surplus:
                    highest_surplus = total_difference
                #total_difference_list.append(total_difference)
                    surplus_day = row[0]
        #return [surplus_day, highest_cash_on_hand]

        return [surplus_day, total_difference]
    
highest_difference_report = cash_difference('cash_on_hand.py')

file_path = Path.cwd()/"summary_report.txt"
file_path.touch()

with file_path.open(mode = "w", encoding = "UTF-8") as file:
    file.write(f"[HIGHEST CASH SURPLUS] DAY: {highest_difference_report[0]}, AMOUNT {highest_difference_report[1]}")


    
  
    


#def total_difference():
#    """
#    - To calculate the difference in cash on hand 
#    """
#    difference = 0
#    current_day = 0
#    next_day = 0
#    fp = Path.cwd()/"cash_on_hand.py"
#    with fp.open(mode="r",encoding="UTF-8",newline="") as file:
#        reader = csv.reader(file)
#        next(reader)
#        for row in reader:
#            difference += float(current_day[1]- next_day[1])



    





#    day = 1,2,3,4,5,6,7,8,9,10,11
#    cash_on_hand = 5408972,4922293,5284056,6335197,6011448,7061570,8469700,9192699,8290871,9130754,9641186
#    for day in range(day,cash_on_hand):
#        total_difference += float(cash_on_hand[0]-cash_on_hand[1])
#   return[day,cash_on_hand]
#print(total_difference)












