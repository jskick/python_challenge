import os
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
Voter = []
County = []
Candidate = []
totalvotes = 0
khan = 0
correy = 0
li = 0
tooley = 0
candidatelist = []
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    if csv.Sniffer().has_header:
        next(csvreader)
    for row in csvreader:
        Voter.append(int(row[0]))
        County.append(row[1])
        Candidate.append(row[2])
    for x in Candidate:
        if x not in candidatelist:
            candidatelist.append(x)
totalvotes = len(Voter)
khancount = Candidate.count("Khan")
correycount = Candidate.count("Correy")
licount = Candidate.count("Li")
tooleycount = Candidate.count("O'Tooley")
khanpercent = format((khancount/totalvotes) * 100, '.2f')
correypercent = format((correycount/totalvotes) * 100, '.2f')
lipercent = format((licount/totalvotes) * 100, '.2f')
tooleypercent = format((tooleycount/totalvotes) * 100, '.2f')
votepercent = [khancount, correycount, licount, tooleycount]
win = max(votepercent)
#dictionaries
candidate = {"name":candidatelist}
percentage = {"percent": [khanpercent,correypercent,lipercent,tooleypercent]}
votecount = {"votes": [khancount,correycount,licount,tooleycount]}
print("Election Results")
print("------------------------")
print("Total Votes:", totalvotes)
print("------------------------")
print(f'{candidate["name"][0]}: {percentage["percent"][0]}% ({votecount["votes"][0]})')
print(f'{candidate["name"][1]}: {percentage["percent"][1]}% ({votecount["votes"][1]})')
print(f'{candidate["name"][2]}: {percentage["percent"][2]}% ({votecount["votes"][2]})')
print(f'{candidate["name"][3]}: {percentage["percent"][3]}% ({votecount["votes"][3]})')
print("-------------------------")
print("Winner:", Candidate[votepercent.index(win)])

f = open("output.txt","a")
f.write("Election Results" "\n")
f.write("--------------------------" "\n")
f.write("Total Votes:" + str(totalvotes) + "\n")
f.write("--------------------------" "\n")
f.write(str(f'{candidate["name"][0]}: {percentage["percent"][0]}% ({votecount["votes"][0]})') + "\n")
f.write(str(f'{candidate["name"][1]}: {percentage["percent"][1]}% ({votecount["votes"][1]})') + "\n")
f.write(str(f'{candidate["name"][2]}: {percentage["percent"][2]}% ({votecount["votes"][2]})') + "\n")
f.write(str(f'{candidate["name"][3]}: {percentage["percent"][3]}% ({votecount["votes"][3]})') + "\n")
f.write("--------------------------" "\n")
f.write("Winner:" + str(Candidate[votepercent.index(win)]) + "\n")
