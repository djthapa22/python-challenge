import os
import csv

# Establishing variables and lists
count = 0
candidate_list = []
individual_can = []
voting_count = []
voter_per = []

# setting the file path
Poll_csv = os.path.join("Resources","election_data.csv")
# Setting the header and skipping it
with open(Poll_csv,newline="") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter =",")
    csv_header = next(csv_file)
    # print(f'Header: {csv_header}')

    # for loop to add a list for total candidates, while setting the count
    for row in csv_reader:
        count += 1 
        candidate_list.append(row[2])
    # Setting another for loop to determine vote count and other metrics for candidate
    for x in set(candidate_list):
        individual_can.append(x)
        Total_V= candidate_list.count(x) 
        
        voting_count.append(Total_V)

        Per = round(((Total_V/count)*100),3)
        voter_per.append(Per)
    #  detrmining the winning vote count and winner
    winner_count = max(voting_count)
    winner = individual_can[voting_count.index(winner_count)]
    

print(f'\n-------------------------\n')
print(f'Election Results\n')   
print('-------------------------\n')
print(f'Total Votes: {count}\n')
print('-------------------------\n')
print(f'Candidates are below:\n')
#  Finding a list of candidats using a for loop
for j in range(len(individual_can)):
    print(f'{individual_can[j]}: {voter_per[j]}% ({voting_count[j]})\n')
print('-------------------------\n')
print(f' The winner is:  {(winner)}\n')
print('-------------------------\n')

output_file= os.path.join("analysis","election_results.txt")
with open(output_file, 'w') as text:
    text.write(f'\n-------------------------\n')
    text.write(f'Election Results \n')   
    text.write('-------------------------\n')
    text.write(f'Total Votes: {count}\n')
    text.write('-------------------------\n')
    text.write(f'Candidates are below: \n')
    for j in range(len(individual_can)):
        text.write(f'{individual_can[j]}: {voter_per[j]}% ({voting_count[j]}) \n')
    text.write('-------------------------\n')
    text.write(f' The winner is:  {(winner)} \n')
    text.write('------------------------- \n')






