# mainsolution.py acts as the coordinating program which executes each python file that has been 
# organised into functions
import overheads, cash_on_hand, profit_loss # import python files as modules

def main():                             # functions for each module exectued in the mainsolution.py
                                        # program
    overheads.overhead_function()
    cash_on_hand.cashonhand_function()
    profit_loss.profitloss_function()

main()

