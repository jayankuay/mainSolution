from pathlib import Path
import matplotlib.pyplot as plt
import csv

# Write a function for cash on hand to be run and called out in mainsolution.py
# Read the csv file to append profit and quantity from the csv.
def cashonhand_function():
    fp = Path.cwd()/"csv_reports"/"Cash on Hand Data.csv" # Create file path to csv folder to read 
                                                          # cash on hand data in csv file
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
        # Neutralise/clean the values by storing variables with value zero
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
        for value in cash_on_hand: # Use for loop to loop through all the values for cash on hand
            current_cash_on_hand = float(value[1]) # Use float to convert current day cash on hand
                                                   # from string
            if current_cash_on_hand > previous_cash_on_hand: # Use if condition for when current cash 
                                                             # on hand is more than previous
                previous_cash_on_hand = current_cash_on_hand # store current cash on hand value as 
                                                             # previous cash on hand to be able to 
                                                             # calculate and loop through other 
                                                             # days' cash on hand
            elif current_cash_on_hand < previous_cash_on_hand: # and if the next day current cash on
                                                               # hand that is being looped to is lesser
                                                               # than currently stored previous cash
                                                               # on hand value
                cash_deficit = previous_cash_on_hand - current_cash_on_hand # Calculate the deficit with
                                                                            # the following formula
                cash_deficit_day = float(value[0]) # The day experiencing the cash on hand deficit will
                                                   # be stored in the variable
                cash_deficits_list.append((cash_deficit_day, cash_deficit)) # Append all stored
                                                                            # variables in 
                                                                            # cash_deficit_day and 
                                                                            # current_cash_on_hand 
                                                                            # to the empty 
                                                                            # cash_deficits_list
            previous_cash_on_hand = current_cash_on_hand # Continue storing back currently looped 
                                                         # current_cash_on_hand variable to the 
                                                         # previous_cash_on_hand again so it is able
                                                         # to continue looping through all values in
                                                         # cash_on_hand_data list to find more
                                                         # days experiencing deficits and get deficit 
                                                         # values
        return cash_deficits_list # Get back the variables in the list
    
    highest_difference_report = cash_difference(cash_on_hand_data) # Store the variables in the list
                                                                   # into another variable 
                                                                   # highest_difference_report
    file_path = Path.cwd() / "summary_report.txt" # The following below will write out the days 
                                                  # experiencing cash deficit and the deficit amount 
                                                  # for those days
                                                  # Create a file path to where the text document file
                                                  # summary_report.txt is stored
    file_path.touch() # Creates a new file in the file path created to the text document 
    
    with file_path.open(mode = "a", encoding = "UTF-8") as file:
        # Use mode "a" to append the data at the start of the text file
        # Use f-strings in order to append the deficit days and deficit amount in the 
        # highest_difference_report variable into the text file.     
        # Iterate through the elements in the list stored in highest_difference_report variable to get
        # the outputs for deficit days and deficit amount and inculde the USD sign for the
        # cash deficit ouputs 
        # Use for loop to call out the elements by representing each entry of elements in the list
        # with day and deficit                          
        for (day, deficit) in highest_difference_report:
            file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{deficit}\n")
    
  
    


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