def total_difference():
    """
    - To calculate the difference in cash on hand 
    """
    cash_on_hand = 5408972,4922293,5284056,6335197,6011448,7061570,8469700,9192699,8290871,9130754,9641186
    for day in range(day,cash_on_hand):
        total_difference += float(cash_on_hand[day]-cash_on_hand[day-1])

print(total_difference)












import csv