#importing necassarcy libraries to analyze csv data
import os
import csv 


total_votes=0
#list for unique candidate name
unique_canadidate=[]
#creatign a dictionary to store both keys and values in it (keys: candiadate name, values: count for each candidate)
unique_total_votes={}



#Storing the file path associated with the csv file
election_data_csv = "PyPoll\\Resources\\election_data.csv"

#opening and reading the csv file
with open(election_data_csv,'r') as csvfile2:
    csvreader2 = csv.reader(csvfile2, delimiter=',')


    #Skipping the header in the data
    header = next(csvreader2)

    #creating a for loop to conduct the analysis
    for row1 in csvreader2:
        #counting the number of rows/months (excluding header)
        total_votes = total_votes + 1

        candidate_name = row1[2]
        # getting each unique candidate name
        if candidate_name not in unique_canadidate:
            unique_canadidate.append(candidate_name)
            #reseting vote for each unique canadiadate to 1 and adding it into the dicationary
            unique_total_votes[candidate_name]=1
        else: 
            #counting the votes for each unique Candidate and adding it into the dicationary 
            unique_total_votes[candidate_name]+=1
       
    #printing the results
    print("Election Results\n")
    print("-------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print("-------------------\n")

            

#inializating my variables
percent =0
winner=0



#looping through the dicationry to print the results and the winner
for i,k in unique_total_votes.items():
    #calculating percent votes
    percent= round(k/total_votes*100,3)
   
   
    #using the max function to find the correpsonding key to the highest value
    winner=max(unique_total_votes, key=unique_total_votes.get)
   
   #printing candidate name percent and total votes for each candidate
    print(f" {i} : {percent}%  ({k})\n")



#print the winner
print("-------------------------\n")
print(f"Winner: {winner}\n")
print("-------------------------\n")




    
#setting the file path for the text file
text_file_path="PyPoll\\Analysis\\Analysis.txt"
#opening and writing into the text file
with open(text_file_path,'w') as text_result2:

    print("Election Results\n",file=text_result2)
    print("-------------------\n",file=text_result2)
    print(f"Total Votes: {total_votes}\n",file=text_result2)
    print("-------------------\n",file=text_result2)

   #looping through the dicationry to print the results and the winner
    for i,k in unique_total_votes.items():
        #calculating percent votes
        percent= round(k/total_votes*100,3)
   
   
    #using the max function to find the correpsonding key to the highest value
        winner=max(unique_total_votes, key=unique_total_votes.get)
   
    #printing candidate name percent and total votes for each candidate
        print(f" {i} : {percent}%  ({k})\n",file=text_result2)

    #print the winner in the text file    
    print("-------------------------\n",file=text_result2)
    print(f"Winner: {winner}\n",file=text_result2)
    print("-------------------------\n",file=text_result2)
   
