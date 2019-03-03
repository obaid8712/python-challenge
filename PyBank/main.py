# Dependencies
import os
import csv

# Path to collect data from the Resources folder
budgetCSV = os.path.join( "Resources", "budget_data.csv")


# Read in the CSV file
with open(budgetCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Loop through the data 
    i=0
    # Declare a place holder for numeric data with out header
    MonthsData=[]
    NetData=[]
    for row in csvreader:    
        i += 1
        if i != 1 : 
            #Add all months data to placeholder for calculation  
            MonthsData.append(row[0])         
            #Add profit and loos data to placeholder for calculation
            NetData.append(row[1])   
    # Total number of months included in the dataset
    numMonth=len(MonthsData)
    # Net total amount of "Profit/Losses" over the entire period
    netProfit=0
    for x in NetData:
        netProfit=netProfit+int(x)
    # The average of the changes in "Profit/Losses" over the entire period
    i=1
    bigNumData=NetData[0]
    sumChange=0
    bigIncrease=0
    bigDecrease=0
    for x in NetData: 
        if i < numMonth : 
            Change = int(NetData[i])-int(x)  
            sumChange=sumChange + Change
            # The greatest Change in profits (amount) over the entire period
            if Change > bigIncrease:
                bigIncrease=Change               
                bigIncMonth=MonthsData[i]
            #The greatest decrease in losses (date and amount) over the entire period
            if Change < bigDecrease:
                bigDecrease=Change               
                bigDecMonth=MonthsData[i]
            i+=1    

    # Calculate Average Change
    avgChange=sumChange/(numMonth-1)
    #Out Put
    print(f"Financial Analysis")
    print(f"------------------------------")
    print(f"Total months : {numMonth}")
    print(f"Total : {netProfit}")
       
    print(f"Average  Change: {'${:,.2f}'.format(avgChange)}")
    print(f"Greatest Increase in Profits: {bigIncMonth} {'${:}'.format(bigIncrease)}")
    print(f"Greatest Decrease in Profits: {bigDecMonth} {'${:}'.format(bigDecrease)}")
    #print(f"Big Increase day {bigIncDay}")

# Specify the file to write to
output_path = os.path.join("output", "PyBank_out.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as text_file:
    # Write the all the output
    print(f"Financial Analysis",file=text_file)
    print(f"------------------------------",file=text_file)
    print(f"Total months : {numMonth}",file=text_file)
    print(f"Total : {netProfit}",file=text_file)
    print(f"Average  Change: {'${:,.2f}'.format(avgChange)}",file=text_file)
    print(f"Greatest Increase in Profits: {bigIncMonth} {'${:}'.format(bigIncrease)}",file=text_file)
    print(f"Greatest Decrease in Profits: {bigDecMonth} {'${:}'.format(bigDecrease)}",file=text_file)

