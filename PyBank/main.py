import os
import csv

csvpath = os.path.join('..', 'Resources', 'BudgetData.csv')
countmonths = 0
netamount = 0
average = 0
money = []
change = []
month = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    if csv.Sniffer().has_header:
        next(csvreader)
    for row in csvreader:
        countmonths += 1
        netamount += int(row[1])
        money.append(int(row[1]))
        month.append(row[0])
    for x in range(1 , len(money)):
        change.append(int(money[x]) - int(money[x-1]))
    greatestrevenue = max(change)
    lowestrevenue = min(change)
average = sum(change) / len(change)
print("Financial Analysis")
print("--------------------------")
print("Total Months:",countmonths)
print("Total:",netamount)
print("Average Change:",average)
print("Greatest Increase in Profits:", month[change.index(max(change))+1], greatestrevenue)
print("Greatest Decrease in Profits:", month[change.index(min(change))+1], lowestrevenue)

f = open("output.txt","a")
f.write("Financial Analysis" "\n")
f.write("---------------------------------------" "\n")
f.write("Total Months:" + str(countmonths) + "\n")
f.write("Total:" + str(netamount) + "\n")
f.write("Average Change:" + str(average) + "\n")
f.write("Greatest Increase in Profits:" + str(month[change.index(max(change))+1]) + str(greatestrevenue) + "\n")
f.write("Greatest Decrease in Profits:" + str(month[change.index(min(change))+1]) + str(lowestrevenue) + "\n")