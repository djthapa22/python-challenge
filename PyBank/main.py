import os
import csv


# The total number of months included in the dataset- Done
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire periodo

# Setting up lists to store info
profit= []
month_count = []
change_M = []
#  Addign in starting variables
Totalp = 0
count = 0
profit_change = 0
start_p = 0

# Tell python to look at the right file path to find budget file
budget_csv = os.path.join("Resources","budget_data.csv")

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter =",")
    csv_header = next(csv_file)
    # print(f'Header: {csv_header}')

    # Running the loop to find values
    for row in csv_reader:
        # Setting the months list
        month_count.append(row[0])
        # style two of month count
        count+= 1
    #   Adding in Profit values to list
        profit.append(row[1])
        Totalp =Totalp + int(row[1])
        #  calcing average values
        final_p = int(row[1])
        change_p = final_p - start_p

        change_M.append(change_p)

        profit_change = profit_change + change_p
        
        average_change = (profit_change/len(month_count))
        start_p = final_p
        #  calculating the values and date to greatest and least values
        greatest_inc = max(change_M)
        greatest_dec = min(change_M)

        inc_date = month_count[change_M.index(greatest_inc)]
        dec_date = month_count[change_M.index(greatest_dec)]

    print("Financial Analysis")
    print("----------------------------------")
    print(f'Total Months: {len(month_count)}')
    print(f'Total Profits: ${str(Totalp)}')
    print(f'Average Change: $ {average_change}')
    print(f'Greatest Increase in Profits: {str(inc_date)} ($ {str(greatest_inc)})')
    print(f'Greatest Decrease in Profits: {str(dec_date)} ($ {str(greatest_dec)})')

# # Finding the right file to place the csv file under
# output_file= os.path.join("analysis","budget_final.txt")
# # setting up the loop for writing the data
# with open(output_file, "w") as datafile:
   

#     datafile.write("Financial Analysis\n")
#     datafile.write("----------------------------------\n")
#     datafile.write(f'Total Months: {len(month_count)}')
#     datafile.write(f'Total Profits: ${str(Totalp)}')
#     datafile.write(f'Average Change: $ {average_change}')
#     datafile.write(f'Greatest Increase in Profits: {str(inc_date)} ($ {str(greatest_inc)})')
#     datafile.write(f'Greatest Decrease in Profits: {str(dec_date)} ($ {str(greatest_dec)})')
