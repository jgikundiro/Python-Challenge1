import os
import csv

# Define the path to the CSV file
csv_file = os.path.join("Resources", "election_data.csv")

# Initialize variables to store election analysis results
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file and perform the election analysis
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)

        # Skip the header row
    header = next(csv_reader)

    # Loop through the remaining rows
    for row in csv_reader:

        # Count the total number of votes cast
        total_votes += 1

        # Track the candidates and their votes
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Prepare the election analysis summary
analysis_summary = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
# Calculate the percentage of votes and the total number of votes for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    analysis_summary += f"{candidate}: {percentage:.3f}% ({votes})\n"

    # Determine the winner based on popular vote
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Add the winner to the analysis summary
analysis_summary += "-------------------------\n"
analysis_summary += f"Winner: {winner}\n"
analysis_summary += "-------------------------\n"

# Print the analysis summary to the console
print(analysis_summary)

# Write the analysis summary to a text file
analysis_output_path = os.path.join("Analysis", "election_analysis.txt")
with open(analysis_output_path, 'w') as analysis_file:
    analysis_file.write(analysis_summary)

print("Analysis summary has been written to 'election_analysis.txt' in the 'analysis' folder.")
