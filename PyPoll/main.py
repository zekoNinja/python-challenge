#importing necassarcy libraries to analyze csv data
import os
import csv 

total_votes=0
unique_canadidate=[]
unique_total_votes={}
dic={}
Total_Votes_list=0

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
        
        

        if candidate_name not in unique_canadidate:
            unique_canadidate.append(candidate_name)
            #reseting vote for each unique canadiadate to 1
            unique_total_votes[candidate_name]=1
        else: 
            unique_total_votes[candidate_name]+=1
       
            

   
           



# print(unique_total_votes)

#still m,
maxpercent=float('-inf')
winner="medo"



percent =0

#ok
for i,k in unique_total_votes.items():
    #ok
    percent= round(k/total_votes*100,3)

    # if percent > maxpercent:
    #         winner=i
            

    print(f" {i} : {percent}% & {k}")


# print(winner)
   


                

        
    # print(unique_canadidate)
                

        
        






        # election_data_list = row1

        # election_list_final.append(election_data_list)

        # County.append(row1[1])
        # Candidate.append(row1[2])


        # # Elecetion_list=zip(Ballot_id,County,Candidate)
        # for row2 in election_list_final:
        #     print(len(election_list_final))
        # break
    # print("Election Results\n")
    # print("-------------------\n")
    # print(f"Total Votes: {total_m}\n")
    # print("-------------------\n")

    