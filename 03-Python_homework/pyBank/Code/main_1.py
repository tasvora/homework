# @Note this code is without using Lambda


# Import Dependencies
import os
import csv


#Variable Declaration
#Defining a list here to hold the data from budget_data.csv
budgetList = []
# holds the Total Profit/Losses
total_profit_loss = 0.00
# holds the Profit/Losses value for current row
gain_loss_current = 0.00
# holds the Profit/Losses value for next row
gain_loss_next = 0.00
# holds the average change between each month.
profitChange = 0.00
# holds the average change for the entire period
averageChange = 0.00
# List to hold the average profit change
profit_loss_List = []
month_name_List = []



#Path for the csv for budget_data.csv
budgetData_csv_path = os.path.join("..", "Resources", "budget_data.csv")
#Debug statement to check the path 
#print(budgetData_csv_path)

#Opening the file to read the data
with open(budgetData_csv_path, newline="") as csvfile:
    #@NOTE: delimiter defined as ","
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # @NOTE: Removing the header
    header = next(csv_reader)

    # Forming a master Lists of lists from the CSV Reader
    # Now each row in the master Lists will be in form of a list
    budgetList = list(csv_reader)
    #Printing the no of Lists in the master List 
    #print(f'budgetList ... {len(budgetList)}')

    # Read through each list of data.
    for row in range(0,len(budgetList)):

        # Profit/Loss of current row(list)
        gain_loss_current = int(budgetList[row][1])
        # Obtaining the total profit loss for the entire period
        total_profit_loss += gain_loss_current
        
        #Checking if the row(list) accessed is not the last in the master list
        # Need to do this otherwise it will throw an error.
        if(row != len(budgetList)-1):
            
            #trying to iterate to the next row(list) in the master List
            next = row + 1
            #Profit/Loss of next row(list)
            gain_loss_next = int(budgetList[next][1])
            # Adding an additional value to the master list and that 
            # will hold the average change between months. This will
            # be at column index 2        
            budgetList[next].append(gain_loss_next-gain_loss_current)

            #Resetting next back to 0, so that everytime we iterate just one row
            next = 0

    #After the entire process, the first row(or list) will 
    #not have an average change, hence putting a default 0 value.
    budgetList[0].append(0)
    
    #Debug statement if wanna view the entire budget List
    #print(budgetList)

    #calculating the Average Change over the entire period
    #first summing up all the changes over each month
    for row in range(0,len(budgetList)):
        profitChange += budgetList[row][2]
        #Processing
        month_name_List.append(budgetList[row][0])
        profit_loss_List.append(budgetList[row][2])


    #Finding the Average change over the entire period
    averageChange = profitChange/(len(budgetList)-1)


    #Prints for Debug..
    #print(f'The no of months ... {len(budgetList)}')
    #print(f'the AVERAGE CHANGE IS .. {value}')

    #print(f'this is the MAX VALUE.... {max(budgetList, key=lambda item: item[2])}')
    #print(f'this is the MIN VALUE.... {min(budgetList, key=lambda item: item[2])}')

    print("File read done")
   

print(month_name_List)
print(profit_loss_List)

maxChange = max(profit_loss_List)
maxIndex = profit_loss_List.index(maxChange)
max_month_Name = month_name_List[maxIndex]
print(f"{maxIndex} {maxChange} {max_month_Name}")

minChange = min(profit_loss_List)
minIndex = profit_loss_List.index(minChange)
min_month_Name = month_name_List[minIndex]
print(f"{minIndex} {minChange} {min_month_Name}")

# Specify the file to write to
output_path = os.path.join("..", "output", "budgetReview2.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as datafile:

    datafile.write("Financial Analysis \n")
    datafile.write("----------------------------\n") 
    #The total number of months included in the dataset
    datafile.write(f"Total Months:  {len(budgetList)} \n")
    datafile.write(f"\n")
    #The net total amount of "Profit/Losses" over the entire period
    datafile.write(f"Total : ${round(total_profit_loss)} \n")
    datafile.write(f"\n")   
    #The average of the changes in "Profit/Losses" over the entire period
    datafile.write(f"Average  Change: ${round(averageChange,2)} \n")
    datafile.write(f"\n")
    #The greatest increase in profits (date and amount) over the entire period
    #Retireving the row(or List) from the budgetList which has Max Profit/Loss Change    
    maxVal = max(budgetList, key=lambda item: item[2])
    #The greatest decrease in losses (date and amount) over the entire period
    #Retireving the row(or List) from the budgetList which has Min Profit/Loss Change
    minVal = min(budgetList, key=lambda item: item[2])

    datafile.write(f"Greatest Increase in Profits:  {max_month_Name}  (${maxChange}) \n")
    datafile.write(f"\n")    
    datafile.write(f"Greatest Decrease in Profits:  {min_month_Name}  (${minChange}) \n")
    
    print("File write done")


 
