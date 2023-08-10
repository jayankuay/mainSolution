from pathlib import Path
import matplotlib.pyplot as plt
import csv

# Write a function for cash on hand to be run and called out in mainsolution.py
# Read the csv file to append profit and quantity from the csv.
def cashonhand_function():
    fp = Path.cwd()/"Cash on Hand Data.csv" # Create file path to read cash on hand data in csv file
    with fp.open(mode="r",encoding="UTF-8",newline="") as file: 
        reader = csv.reader(file)
        next(reader)  # Skip header

# Create empty list to store cash on hand by day respectively
        cash_on_hand_data = []

        for row in reader:
            cash_on_hand_data.append(row)

# Create a function that finds days experiencing cash on hand deficit over the 90 days
    def cash_difference(cash_on_hand):
        """
        - Calculates the deficit in the cash on hand and finds the days experiencing cash on hand
        deficit
        """
        # Neutalise/clean the values by storing variables with value zero
        current_cash_on_hand = 0
        previous_cash_on_hand = 0
        cash_deficit = 0
        cash_deficit_day = 0
        cash_deficits_list = []
        # please ignore this first
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
        # use 'for loop' to look throught the cash on hand csv file
        # convert data into from string to float as money as decimal point
        
      
        # add the deficit day and total amount of the cash deficit into the list
        # use return as the function will send values back to the main program
      
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
    

    # creating a general variable to store the total data
    highest_difference_report = cash_difference(cash_on_hand_data)


    # create a path to txt file
    # use .cwd() to represent your current location in the file system 
    # use .touch() to create a file(summary_.txt)
    file_path = Path.cwd() / "summary_report.txt"
    file_path.touch()
    

    # write the txt file using the data in csv file 
    # use 'with' statement to make the code cleaner and more readable
    # use .open() to return the file
    # using the mode="a" to append the all the data in one summary_report.txt.
    # use encoding="UTF-8" to keep things simple
    # use .write()method to write data in a plain text file
    # use f string to print mutiple variable
    with file_path.open(mode = "a", encoding = "UTF-8") as file:
        for (day, deficit) in highest_difference_report:
            file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: {deficit}\n")
    
  
    

# please ignore this first
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
#for highest_surplus_day, highest_surplus in highest_difference_report:
        #if highest_surplus > 0:
            #file.write(f"[HIGHEST CASH SURPLUS] DAY: {highest_difference_report[0]}, AMOUNT: {highest_difference_report[1]}\n")
        #if highest_difference_report[1] < 0: