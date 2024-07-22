#Module 3 Challenge Pypoll
import os
import csv
csvpath = "Resources/election_data.csv"



print("Election Results")
print("~~~~~~~~~~~~~~~~")

total_votes = 0
candidate_votes = {}

with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        candidate = row[2] 
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
#This makes sure that the code prints both the number of votes and the candidates name, by looping through both columns
print(f"Total Votes: {total_votes}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {votes} {percentage:.1f}%")
#the for line makes sure that the percentage and print message are connected to the previous for loop
#I rounded the percentage to reduce the number of decimals
total_votes = 0
winner = {}
candidate_votes = 0

with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        candidate = row[2]

        if candidate in winner:
            winner[candidate] += 1
        else:
            winner[candidate] = 1

        if winner[candidate] > candidate_votes:
            candidate_votes = winner[candidate]
            winning_candidate = candidate
#This for loop loops through to find the person with the total number of votes, combining "winner" and "candidate"
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Winner: {winning_candidate}")
print("~~~~~~~~~~~~~~~~~~~~~~")



            



    
    
    
