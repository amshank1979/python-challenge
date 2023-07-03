import csv

# Path to the budget data CSV file

# Read the budget data CSV file
with open("./Resources/budget_data.csv") as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)  # Skip the header row

    # Initialize variables
    total_months = 0
    net_total = 0
    previous_profit = 0
    changes = []
    max_increase = 0
    max_decrease = 0
    max_increase_month = ""
    max_decrease_month = ""

    # Loop through each row in the CSV
    for row in csv_reader:
        # Extract the date and profit/loss from the row
        date = row[0]
        profit = int(row[1])

        # Calculate total months and net total
        total_months += 1
        net_total += profit

        # Calculate the change in profit/loss from the previous month
        if previous_profit != 0:
            change = profit - previous_profit
            changes.append(change)

            # Check for maximum increase and decrease
            if change > max_increase:
                max_increase = change
                max_increase_month = date
            if change < max_decrease:
                max_decrease = change
                max_decrease_month = date

        # Update the previous profit/loss
        previous_profit = profit

    # Calculate the average change
    average_change = sum(changes) / len(changes)

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")
print(f"Analysis exported to ./analysis/financial_analysis.txt")

# Export the analysis to a text file
with open("./analysis/financial_analysis.txt", 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${round(average_change, 2)}\n")
    file.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n")
    file.write(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")
 