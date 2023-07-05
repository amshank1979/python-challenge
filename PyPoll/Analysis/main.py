import csv

# Read the CSV file and initialize variables
file_path = "./Resources/election_data.csv"
total_votes = 0
candidates = {}
winner_votes = 0
winner = ""

# Read the CSV file
with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    # Iterate over each row in the CSV file
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # Update the candidate's vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    # Check if the candidate is the current winner
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the election results to a text file
output_file = "election_results.txt"
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print(f"Election results have been saved to {output_file}.")
