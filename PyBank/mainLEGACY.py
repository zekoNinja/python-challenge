# #importing necassarcy libraries to analyze csv data
# import os
# import csv 


# #Storing the file path associated with the csv file
# Budget_data_csv = "PyBank\\Resources\\budget_data.csv"

# #
# with open(Budget_data_csv, 'r') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')

#     header = next(csvreader)
#     total_change=0
#     next_value = 0
#     change=0
#     net_amount1=0
#     total_m= 0
#     total_net_amount=0
#     for row in csvreader:
#         total_m = total_m + 1
#         net_amount = int(row[1])
#         total_net_amount=net_amount+total_net_amount
        
#         if next_value !=0:
#             change=net_amount-next_value
#             print(change)
        
#     print("Total Months:" + " " + str(total_m)) 
#     print("Total:" +" " +"$"+str(total_net_amount))  
            


        

#         # #changes in profit/losses over entire period 
#         # net_amount1 = int(row[1])
#         # if next_value !=0 :
#         #     change =net_amount1 - next_value
#         #     # print(change)
#         # total_change=change+total_change
#         # #calculating average dividing by total_m and since first loop change is 0 taking 1 out of counter
#         # average = round(total_change/85,2)
    
#         # #assigning the previous value
#         # next_value=net_amount1
       
         

          
#     # print(change)  
#     # print(average)

# # #Defining Financial Analysis function to analyze data from the budget data file
# # def Financial_Analysis(budget_data):
# #     print("Financial Anlysis\n")
# #     print("---------------------\n")

# #     Total_motnths=int(len(budget_data[0]))
# #     print("Total Months:" + str(Total_motnths))






# # # Financial_Analysis()





