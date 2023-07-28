from pathlib import Path
import matplotlib.pyplot as plt
import csv

def total_difference(file):
    """
    - Calculate the difference in the cash on hand
    """
    day_of_cash_on_hand = 0
    current_cash_on_hand = 0
    previous_cash_on_hand = 0
    total_difference = 0
    deficit_value = 0
    surplus_value = 0

    fp = Path.cwd()/"Cash on hand.csv"
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
        
            current_cash_on_hand = float(row[1])
            previous_cash_on_hand= float(row[1-1])
            total_difference = current_cash_on_hand - previous_cash_on_hand
            if current_cash_on_hand > previous_cash_on_hand:
                surplus_value = total_difference
            elif current_cash_on_hand < previous_cash_on_hand:
                deficit_value = abs(total_difference)
            else:
                total_difference = total_difference
    return(file)

file_path = Path.cwd() / "summary_report.txt"
file_path.touch()
    
with file_path.open(mode = "w", encoding = "UTF-8") as file:
    file.write(f"[Highest Surplus Value:$] {total_difference}")
    file.write(f"[Highest Deficit Value:$] {abs(total_difference)}")
            
           
                
                
                
               

                 


























#def cash_difference():
#    """
#    - TO calculate the difference in cash on hand
#    """
#    total_difference = 0
#    difference = 0
#    total_difference_list = 0
#    fp = Path.cwd()/"cash_on_hand.py"
#    with fp.open(mode="r",encoding="UTF-8",newline="") as file:
#        reader = csv.reader(file)
#        next(reader)
#        for row in reader:
#            if difference[1] < difference[row-1]:
#                total_difference = difference[row-1] - difference[1]
#                total_difference_list.append(total_difference)
#        return[total_difference_list]
    
#highest_difference_report = cash_difference['cash_on_hand.py']

#file_path = Path.cwd()/"summary_report.txt"
#file_path.touch()

#with file_path.open(mode = "w", encoding = "UTF-8") as file:
#    file.write(f"[Highest increment]=$ {highest_difference_report[1]}")


    
  
    


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
