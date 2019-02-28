import os
import csv

# Path to collect data from the Resources folder
electionCSV = os.path.join( "Resources", "election_data.csv")

# Read in the CSV file
with open(electionCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Loop through the data 
    i=0
    totalId=0
    # Declare a place holder for numeric data with out header
    Candidate=[]
    CastVoteEach=["0","0","0","0"]
    #CastVoteEach=[]
    #while i<len(Candidate):
    #    CastVoteEach[i]=(str("0"))
    #    i=i+1
    #for x in CastVoteEach:  
    #    print(x)
    # Function for Counting vote for each candidate 
    def countVote(vote):
        j=0
       
        while j < len(Candidate):
            if vote == Candidate[j]:
                CastVoteEach[j]=int(CastVoteEach[j])+1
            j=j+1
    
    #numData1=[]
    j=0
    i=0
    for row in csvreader:

        i = i+1
        if i != 1: # Discard the header row
            #The total number of votes cast
            totalId+=1
            #A complete list of candidates who received votes
            y=0
            for x in Candidate:
                if row[2] == x:  
                    y=1 
            if y == 1:                
                y=0
            else:
                Candidate.append(str(row[2]))
                y=0 

            countVote(row[2])             
  
#Out Put

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalId} ")
k=0
#find the winer
HighestVote=max(CastVoteEach)

for x in CastVoteEach:
    if HighestVote==x:
        winindex=k
    k+=1
k=0
for x in Candidate:
    percent=CastVoteEach[k]*100/totalId    
    print(f"{x}: {'{:,.3f}%'.format(percent)} ({CastVoteEach[k]})")
    k+=1  
print("-------------------------")    
print(f"Winner: {Candidate[winindex]}")

# Specify the file to write to
output_path = os.path.join("output", "PyPoll_out.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as text_file:
    # Write the all the output 
    print("Election Results",file=text_file)
    print("-------------------------",file=text_file)
    print(f"Total Votes: {totalId} ",file=text_file) 
    k=0
    for x in Candidate:
        percent=CastVoteEach[k]*100/totalId    
        print(f"{x}: {'{:,.3f}%'.format(percent)} ({CastVoteEach[k]})",file=text_file)
        k+=1  
    print("-------------------------",file=text_file)    
    print(f"Winner: {Candidate[winindex]}",file=text_file)