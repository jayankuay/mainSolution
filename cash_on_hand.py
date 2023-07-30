from pathlib import Path
import matplotlib.pyplot as plt
import csv

fp = Path.cwd()/"Cash on Hand.csv"
with fp.open(mode="r",encoding="UTF-8",newline="") as file:
    reader = csv.reader(file)
    next(reader)

    cash_on_hand_data = []
    
    for row in reader:
        cash_on_hand_data.append(row)

def cash_difference(cash_on_hand):
    """
    - Calculate the difference in the cash on hand
    """
    current_cash_on_hand = 0
    previous_cash_on_hand = 0
    cash_deficit = 0
    cash_deficit_day = 0
    cash_deficits_list = []
            #current_cash_on_hand = float(row[1])
            #if previous_cash_on_hand > 0 and current_cash_on_hand > previous_cash_on_hand:
            #    total_difference = current_cash_on_hand - previous_cash_on_hand
            #previous_cash_on_hand = current_cash_on_hand
            #if total_difference > highest_surplus:
            #    highest_surplus =  total_difference
            #    highest_surplus_day = row[0]
            #current_cash_on_hand = float(row[1])
            #if previous_cash_on_hand > 0 and current_cash_on_hand < previous_cash_on_hand:
            #    cash_deficit = previous_cash_on_hand - current_cash_on_hand
            #    cash_deficit_day = row[0]
            #previous_cash_on_hand = current_cash_on_hand  
    for value in cash_on_hand:
        current_cash_on_hand = float(value[1])
        if current_cash_on_hand > previous_cash_on_hand:
            previous_cash_on_hand = current_cash_on_hand
        elif current_cash_on_hand < previous_cash_on_hand:
            cash_deficit = previous_cash_on_hand - current_cash_on_hand
            cash_deficit_day = float(value[0])
            cash_deficits_list.append((cash_deficit_day, cash_deficit))
        previous_cash_on_hand = current_cash_on_hand
    return cash_deficits_list
    
highest_difference_report = cash_difference(cash_on_hand_data)

file_path = Path.cwd() / "summary_report.txt"
file_path.touch()
    
with file_path.open(mode = "w", encoding = "UTF-8") as file:
    #for highest_surplus_day, highest_surplus in highest_difference_report:
        #if highest_surplus > 0:
            #file.write(f"[HIGHEST CASH SURPLUS] DAY: {highest_difference_report[0]}, AMOUNT: {highest_difference_report[1]}\n")
        #if highest_difference_report[1] < 0:
    for day, deficit in highest_difference_report:
        file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: {deficit}\n")
    
  
    


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
