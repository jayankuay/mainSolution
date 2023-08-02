from pathlib import Path
import matplotlib.pyplot as plt
import csv
fp = Path.cwd()/"profit and loss.csv"
with fp.open(mode="r",encoding="UTF-8",newline="") as file:
    reader = csv.reader(file)
    next(reader)
    
    net_profit_data= []

for row in reader:
        net_profit_data.append(row)

def profit_loss_difference(profit_and_loss):
    """
    - Calculate the difference in the profits
    """
current_net_profit=0
previous_net_profit=0
for value in profit_and_loss:
     current_net_profit=float(value(4))
     if current_net_profit > previous_net_profit:
          previous_net_profit=current_net_profit
    
