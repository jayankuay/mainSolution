from pathlib import Path
import matplotlib.pyplot as plt
import csv
# Write a function for overhead to be run and called out in mainsolution.py
def overhead_function(): 
    fp = Path.cwd()/"csv_reports"/"Overheads Data.csv" # Create file path to csv folder to read 
                                                       # overheads data in csv file
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file) 
        next(reader) # skip header 

        overheads = [] # Create empty list to store all the data
        # Append overheads and percentage back into empty list
        for row in reader:
            overheads.append(row)
        
    # Create a function that finds highest overhead expense over the 90 days
    def highest_overhead_expense(expense):
        """
        Will find the highest overhead expense incurred over 90 day period of running the business
        """
        # Neutralise/clean the values to zero
        highest_expense = 0
        highest_overhead = 0
        for value in expense: # Use a for loop to run through every overhead expense and percentage
            overhead = float(value[1]) # Convert data from string to float
            # Use if condition to find when a looped overhead value is higher than current highest 
            # overhead value
            if overhead > highest_overhead:
                highest_overhead = overhead # When overhead value is higher than current highest 
                                            # overhead, replace it and store it under 
                                            # highest_overhead variable
                highest_expense = value[0] # Call out highest expense name from the list with index
                                           # postion zero
        return [highest_expense, highest_overhead] # Get the data for highest expense and highest
                                                   # overhead percentage into a list
    highest_overhead_report = highest_overhead_expense(overheads)  # Use highest_overhead_report 
                                                                   # variable to store values
                                                                   # in the list

# The following will write out the data found for highest overhead expense and its percentage
# Create a file path to where the text document file region_report.txt is stored
    file_path = Path.cwd()/"summary_report.txt"
    file_path.touch() # Creates a new file in the file path created to the text document

    with file_path.open(mode = "a", encoding = "UTF-8") as file: # Use mode "a" to append the data
                                                                 # correspondingly into the txt file
        # Use f-strings in order to append the stored highest overhead expense and percentage in the 
        # highest_overhead_report variable into the text file.     
        # Iterate through the elements in the list stored in highest_overhead_report variable to get the
        # outputs for highest overhead expense and percentage and inculde the % sign for the
        # percentage outputs to indicate proportion of operating expenses spent on the highest 
        # overhead.                                                    
        file.write(f"[HIGHEST OVERHEAD] {highest_overhead_report[0]}: {highest_overhead_report[1]}%\n")