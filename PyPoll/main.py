# Programm for PyPoll
# Import dependancy
import os
import csv

# Path to collect data from the Resources folder
electionCSV = os.path.join( "Resources", "election_data.csv")

# Read in the CSV file
with open(electionCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',') 
        
    # Declare a place holder for name of candidate
    Candidate=[]
    # Declare a dictionary to hole candidate name and vote cast
    dic_poll={}    
    
    # Function for Counting vote for each candidate 
    def countVote(vote):
               
        for x,y  in dic_poll.items():
            if vote == x:
                y=int(dic_poll.get(x))+1
                dic_poll[x]=y
    # Loop through the data
    i=0
    for row in csvreader:

        i = i+1
        if i != 1: # Discard the header row
                          
            #Find a list of candidates who received votes
            y=0
            for x in Candidate:
                if row[2] == x:  
                    y=1 
            if y == 1:                
                y=0
            else:
                Candidate.append(str(row[2]))
                dic_poll[str(row[2])]=0
                y=0 

            
            # Call function to count the vote
            countVote(row[2])             

# The total number of votes cast
total_vote_cast=0
max_vote=0
winner=""
for x, vote_cast in dic_poll.items():
    # Find total vote casted
    total_vote_cast=total_vote_cast + vote_cast
    # Find Winner
    if max_vote < vote_cast:
        max_vote=vote_cast
        winner=x
# Out put of Election Results
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_vote_cast} ")
print("-------------------------")
# Print a list of candidate name with result 
for name, vote_cast in dic_poll.items() :
    percent_count=vote_cast*100/total_vote_cast
    print(f"{name}: {'{:,.3f}%'.format(percent_count)} ({vote_cast})")
# Print the winner's name
print("-------------------------")
print(f"The Winner is {winner}")

# Specify the file to write 
output_path = os.path.join("output", "PyPoll_out.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as text_file:
    # Write the all the output 
    print("Election Results",file=text_file)
    print("-------------------------",file=text_file)
    print(f"Total Votes: {total_vote_cast} ",file=text_file) 
    print("-------------------------",file=text_file)
    for name, vote_cast in dic_poll.items() :
        percent_count=vote_cast*100/total_vote_cast
        print(f"{name}: {'{:,.3f}%'.format(percent_count)} ({vote_cast})",file=text_file)
    print("-------------------------",file=text_file)    
    print(f"Winner: {winner}",file=text_file)