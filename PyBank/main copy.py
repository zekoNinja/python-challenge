#importing necassarcy libraries to analyze csv data
import os
import csv 

Budget_info= []

#Storing the file path associated with the csv file
Budget_data_csv = "PyBank\\Resources\\budget_data.csv"

#
with open(Budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    total_change=0
    next_value = 0
    change=0
    net_amount1=0
    total_m= 0
    total_net_amount=0
    max_value=0
    min_value=0
    max_date=0
    min_date=0

    for row in csvreader:
        total_m = total_m + 1
        net_amount = int(row[1])
        total_net_amount=net_amount+total_net_amount

        #changes in profit/losses over entire period 
        net_amount1 = int(row[1])
       
        if next_value !=0 :
            change =net_amount1 - next_value
            # print(change)
        total_change=change+total_change
        #calculating average dividing by total_m and since first loop change is 0 taking 1 out of counter
        if total_m-1 !=0:
            average = round(total_change/(total_m-1),2)
    
        if(change > max_value):
            max_value=change
            max_date=row[0]

        elif(change<min_value):
            min_value=change
            min_date=row[0]

        #assigning the previous value
        next_value=net_amount1

       

    else:
        change=0


      

       
        # exit 

    print("Total Months:" + " " + str(total_m)) 
    print("Total:" +" " +"$"+str(total_net_amount))    
    # print(change)  
    print("Average Change:" + " " + "$"+str(average))
    print(f"Greatest Increase in Profits: {max_date} (${max_value})")
    print(f"Greatest Decerease in Profits: {min_date} (${min_value})")
    


text_file_path="PyBank\\Analysis\\Analysis.txt"
with open(text_file_path,'w') as text_result:

     print("Total Months:" + " " + str(total_m), file=text_result) 
     print("Total:" +" " +"$"+str(total_net_amount),file=text_result)    
    # print(change)  
     print("Average Change:" + " " + "$"+str(average),file=text_result)
     print(f"Greatest Increase in Profits: {max_date} (${max_value})",file=text_result)
     print(f"Greatest Decerease in Profits: {min_date} (${min_value})",file=text_result)
    





# #Defining Financial Analysis function to analyze data from the budget data file
# def Financial_Analysis(budget_data):
#     print("Financial Anlysis\n")
#     print("---------------------\n")

#     Total_motnths=int(len(budget_data[0]))
#     print("Total Months:" + str(Total_motnths))







# # Financial_Analysis()





