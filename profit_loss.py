from pathlib import Path
import matplotlib.pyplot as plt
import csv

fp = Path.cwd()/"profit-and-loss.csv"
with fp.open(mode="r",encoding="UTF-8",newline="") as file:
    reader = csv.reader(file)
    next(reader)
    
    net_profit_data= []

    for row in reader:
        net_profit_data.append([row[0], row[4]])

    def profit_loss_difference(profit_and_loss):
        """
        - Calculate the difference in the profits
        """
        current_net_profit=0
        previous_net_profit=0
        loss_in_profit = 0
        loss_in_profit_day = 0
        profit_and_loss_list =[]
        for value in profit_and_loss:
            current_net_profit=float(value[1])
            if current_net_profit > previous_net_profit:
                previous_net_profit = current_net_profit
            elif current_net_profit < previous_net_profit:
                loss_in_profit = previous_net_profit - current_net_profit
                loss_in_profit_day = value[0]
                profit_and_loss_list.append((loss_in_profit_day, loss_in_profit))
            previous_net_profit = current_net_profit
        return profit_and_loss_list
    profit_loss_report = profit_loss_difference(net_profit_data)
    print(profit_loss_report)
    file_path = Path.cwd() / "summary_report.txt"
    file_path.touch()

    with file_path.open(mode = "a", encoding = "UTF-8") as file:
        for (day, deficit_profit) in profit_loss_report:
            file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: {deficit_profit}\n")
             
            
    
