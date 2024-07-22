#Module 3 Challenge
import os
import csv
csvpath = "Resources/budget_data.csv"

print("Financial Analysis")
print("~~~~~~~~~~~~~~~~~~~~")

net_profit_loss = 0

with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for i, row in enumerate(csv_reader):
        if i == 0:
            net_profit_loss = float(row[1])
        else:
            net_profit_loss += float(row[1])
#The profit loss loop had to be set before the others so that we could calculate the changes
total_months = 0
changes_in_profit_loss = []

with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    previous_profit_loss = None
    
    for i, row in enumerate(csv_reader):
        current_profit_loss = float(row[1])
        
        if previous_profit_loss is not None:
            change = current_profit_loss - previous_profit_loss
            changes_in_profit_loss.append(change)
            #We subtract the profit loss to find the change, that way we can average the changes
        previous_profit_loss = current_profit_loss
        total_months += 1
        #I put the total months in the loop, but I can take total months outside of the loop and the rest of the code will still work
average_change = sum(changes_in_profit_loss) / len(changes_in_profit_loss)

print(f"Total Months: {total_months}")
print(f"Total Profit/Loss: ${net_profit_loss}")
print(f"Average Change: ${average_change:.1f}")

greatest_increase=0
greatest_date="" #Greatest date has empty double quotes because the values in that column have months and days (words and numbers)
with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    previous_profit_loss = None
    
    for i, row in enumerate(csv_reader):
        current_profit_loss = float(row[1])
        current_date= row[0]
        #This tells the computer which rows to look through
        if previous_profit_loss is not None:
            change = current_profit_loss - previous_profit_loss
            if change > greatest_increase:
                greatest_increase = change
                greatest_date=current_date
        #This is stating that the computer should search the column to find the greatest increase in profit, based on the profit loss
        previous_profit_loss = current_profit_loss

if greatest_increase > 0:
    print(f"Greatest Increase in profits: {greatest_date}  (${greatest_increase})")


greatest_decrease = 0
decrease_date = ""
previous_profit_loss = None

with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        current_profit_loss = float(row[1])
        current_date = row[0]

        if previous_profit_loss is not None:
            change = current_profit_loss - previous_profit_loss
            if change < greatest_decrease:
                greatest_decrease = change
                decrease_date = current_date
        
        previous_profit_loss = current_profit_loss

    if greatest_decrease < 0:
        print(f"Greatest Decrease in profits: {decrease_date} (${greatest_decrease})")
#This code functions the same as the previous, except "<" symbol is used to find the greatest decrease in profit change, above the 
# ">" symbol was using to find the greatest increase
    



    




