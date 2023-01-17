# adding import os and csv
import os
import csv


# Setting up lists to store info
month_count = []
change_M = []
#  Addign in starting variables
Totalp = 0
count = 0
profit_change = 0
currentp = 0
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
        
        # count of months; style 2
        count += 1
        
        # Setting up the total profit for the period
        currentp = int(row[1])
        Totalp+= currentp
        
        # starting if statement to set value of profit for starting to be same as current
        if(count == 1):
            start_p = currentp
            continue
        # calcing change in profit, along with adding to values to lists (month count), (profit change),
        else:
            profit_change = currentp - start_p
            month_count.append(row[0])
            change_M.append(profit_change)
        #    set the loop so that starting p is set to current p
            start_p = currentp

    # Calc the average profit change 
    Sum_p = sum(change_M)
    average_p = round((Sum_p)/(len(month_count)),2)

    # calc th value for highest and lowest change
    greatest_inc = max(change_M)
    greatest_dec = min(change_M)
    #  find the index value of highest and lowest
    inc_date = month_count[change_M.index(greatest_inc)]
    dec_date = month_count[change_M.index(greatest_dec)]

    

    #  set a unique method for printing so that line breaks look cleaner
    Output = (
    "\nFinancial Analysis\n"
   "----------------------------------\n"
   f'Total Months: {len(month_count)+1}\n'
    f'Total Profits: ${str(Totalp)}\n'
     f'Average Change: $ {average_p}\n'
    f'Greatest Increase in Profits: {str(inc_date)} ($ {str(greatest_inc)})\n'
    f'Greatest Decrease in Profits: {str(dec_date)} ($ {str(greatest_dec)})\n'
    )
print(Output)

# # Finding the right file to place the csv file under
output_file= os.path.join("analysis","budget_final.txt")
# # setting up the loop for writing the data
with open(output_file, "w") as datafile:
    datafile.write(Output)

