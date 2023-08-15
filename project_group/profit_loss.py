from pathlib import Path
import matplotlib.pyplot as plt
import csv
# Write a function for cash on hand to be run and called out in mainsolution.py
# Read the csv file to append days and net profit from the csv.
def profitloss_function():
    fp = Path.cwd()/"csv_reports"/"profit-and-loss.csv" # Create file path to csv folder to read cash
                                                        # on hand data in csv file
    with fp.open(mode="r",encoding="UTF-8",newline="") as file:
        reader = csv.reader(file)
        next(reader) # Skip header
    
        net_profit_data= []  # Create empty list to store all the data
        # Append days and net profit respectively back into empty list

        for row in reader:
            net_profit_data.append([row[0], row[4]])
# Create a function that finds days loss in profit over the 90 days
        def profit_loss_difference(profit_and_loss):
            """
            - Calculates the loss in profits througout the 90 days
            """
            # Neutralise/clean the values by storing variables with value zero
            current_net_profit=0
            previous_net_profit=0
            loss_in_profit = 0
            loss_in_profit_day = 0
            profit_and_loss_list =[]

            for value in profit_and_loss:  # Use for loop to loop through all the values for cash on hand
                current_net_profit=float(value[1]) # Use float to convert current day net profit
                                                   # from string to float
                if current_net_profit > previous_net_profit:  # Use if condition for when current day
                                                              # net profit is more than previous net 
                                                              # profit
                    previous_net_profit = current_net_profit  # store current net profit value as 
                                                             # previous net profit to be able to 
                                                             # calculate and loop through other 
                                                             # days' net profit
                elif current_net_profit < previous_net_profit: # and if the next day current net profit
                                                               # that is being looped to is lesser
                                                               # than currently stored previous net
                                                               # profit value
                    loss_in_profit = previous_net_profit - current_net_profit # Calculate the loss in
                                                                            # profit with the 
                                                                            # following formula
                    loss_in_profit_day = value[0]  # The day experiencing the loss in profit will
                                                   # be stored in the variable
                    profit_and_loss_list.append((loss_in_profit_day, loss_in_profit)) # Append all
                                                                            # stored variables in 
                                                                            # loss_in_profit_day and 
                                                                            # loss_in_profit
                                                                            # to the empty 
                                                                            # profit_and_loss_list
                previous_net_profit = current_net_profit # Continue storing back currently looped 
                                                         # current_net_profit variable to the 
                                                         # previous_net_profit again so it is able
                                                         # to continue looping through all values in
                                                         # net_profit_data list to find more
                                                         # days experiencing loss in profit and get 
                                                         # loss in profit values
            return profit_and_loss_list # Get back the variables in the list
        profit_loss_report = profit_loss_difference(net_profit_data) # Store the variables in the list
                                                                   # into another variable 
                                                                   # profit_loss_report
        
        file_path = Path.cwd() / "summary_report.txt"  # The following below will write out the days 
                                                  # experiencing loss in net profit and the 
                                                  # loss in profit amount for those days
                                                  # Create a file path to where the text document file
                                                  # summary_report.txt is stored
        file_path.touch() # Creates a new file in the file path created to the text document 

        with file_path.open(mode = "a", encoding = "UTF-8") as file:
        # Use mode "a" to append the data correspondingly into the txt file 
        # Use f-strings in order to append the loss in profit days and loss in profit amount in the 
        # profit_loss_report variable into the text file. 
        # Use for loop to loop through all the elements and represent each entry of elements in the list
        # with day and deficit_profit       
        # Iterate through the elements in the list stored in profit_loss_report variable to get
        # the outputs for days experiecing loss in net profit and the loss in profit amount and 
        # inculde the USD sign for the loss in profit amount ouputs 
                
            for (day, deficit_profit) in profit_loss_report:
                file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{deficit_profit}\n")
             
            
    
