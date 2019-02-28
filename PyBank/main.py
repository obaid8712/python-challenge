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
    numData0=[]
    numData=[]
    for row in csvreader:    
        i = i +1
        if i != 1 :   
            numData0.append(row[0])         
            #Add profit and loos data to placeholder for calculation
            numData.append(row[1])   
    # Total number of months included in the dataset
    numMonth=len(numData)
    # Net total amount of "Profit/Losses" over the entire period
    netProfit=0
    for x in numData:
        netProfit=netProfit+int(x)
    # The average of the changes in "Profit/Losses" over the entire period
    i=1
    bigNumData=numData[0]
    sumChange=0
    bigIncrease=0
    bigDecrease=0
    for x in numData: 
        if i < numMonth : 
            Increse = int(numData[i])-int(x)  
            sumChange=sumChange + Increse
            # The greatest increase in profits (amount) over the entire period
            if Increse > bigIncrease:
                bigIncrease=Increse               
                bigIncDay=numData0[i]
            #The greatest decrease in losses (date and amount) over the entire period
            if Increse < bigDecrease:
                bigDecrease=Increse               
                bigDecDay=numData0[i]
            i+=1    

    # Calculate Average Change
    avgChange=sumChange/(numMonth-1)
    #Out Put
    print(f"Financial Analysis")
    print(f"------------------------------")
    print(f"Total months : {numMonth}")
    print(f"Total : {netProfit}")
    #for x in numData:
    #    print(f"data {x}")
    #print(f"Average  Change: {avgChange}")
    print(f"Average  Change: {'${:,.2f}'.format(avgChange)}")
    print(f"Greatest Increase in Profits: {bigIncDay} {'${:}'.format(bigIncrease)}")
    print(f"Greatest Decrease in Profits: {bigDecDay} {'${:}'.format(bigDecrease)}")
    #print(f"Big Increase day {bigIncDay}")

# Specify the file to write to
output_path = os.path.join("output", "PyBank_output.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as text_file:
    # Write the all the output
    print(f"Financial Analysis",file=text_file)
    print(f"------------------------------",file=text_file)
    print(f"Total months : {numMonth}",file=text_file)
    print(f"Total : {netProfit}",file=text_file)
    print(f"Average  Change: {'${:,.2f}'.format(avgChange)}",file=text_file)
    print(f"Greatest Increase in Profits: {bigIncDay} {'${:}'.format(bigIncrease)}",file=text_file)
    print(f"Greatest Decrease in Profits: {bigDecDay} {'${:}'.format(bigDecrease)}",file=text_file)

