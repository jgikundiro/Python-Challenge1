import os
import csv

# Define the path to the CSV file
csv_file = os.path.join("Resources", "budget_data.csv")

# Initialize variables to store financial analysis results
total_months = 0
net_profit = 0
average_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

# Lists to store monthly changes in profit/loss
profit_changes = []

with open(csv_file, 'r') as file:
    csv_reader =  csv.reader(file)

     # Skip the header row
    header = next(csv_reader)

    # Initialize variables for the first row
    first_row = next(csv_reader)
    prev_month = int(first_row[1])
    total_months = 1
    net_profit = int(first_row[1])

     # Loop through the remaining rows
    for row in csv_reader:

        # Calculate the total number of months
        total_months +=1

        # Calculate the net total amount of profit/losses
        net_profit += int(row[1])

         # Calculate the change in profit/loss from the previous month
        current_month = int(row[1])
        profit_change = current_month - prev_month
        profit_changes.append(profit_change)
        prev_month = current_month

        # Find the greatest increase and corresponding date
        if profit_change > greatest_increase:
            greatest_increase = profit_change
            greatest_increase_date = row[0]
        
        # Find the greatest decrease and corresponding date
        if profit_change < greatest_decrease:
            greatest_decrease = profit_change
            greatest_decrease_date = row[0]

# Calculate the average change in profit/loss over the entire period
average_change = sum(profit_changes) / len(profit_changes)

# Prepare the analysis summary
analysis_summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_profit}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the analysis summary to the console
print(analysis_summary)

# Write the analysis summary to a text file
analysis_output_path = os.path.join("Analysis", "financial_analysis.txt")
with open(analysis_output_path, 'w') as analysis_file:
    analysis_file.write(analysis_summary)

print("Analysis summary has been written to 'financial_analysis.txt' in the 'analysis' folder.")
