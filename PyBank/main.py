import os
import csv


# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period


months = []



# Tell python to look at the right file path to find budget file
budget_csv = os.path.join("Resources","budget_data.csv")

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter =",")
    csv_header = next(csv_file)
    # print(f'Header: {csv_header}')

    for row in csv_reader:
        months.append(row[0])




# Finding the right file to place the csv file under
output_file= os.path.join("analysis","budget_final.csv")
# setting up the loop for writing the data
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow("Financial Analysis")
    writer.writerow("----------------------------------")
    writer.writerow(f'Total Months: {len(months)}')
