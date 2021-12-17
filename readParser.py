import re
import csv
import infoFill

#to make input hidden
from getpass import getpass

#description:   parse through card reader string iput
#input:         card reader string input
#returns:       [lastname, FirstInitial, uniquename]
def parseCardInfo(cardReaderInput):
    #validation regex: 
    if not re.match("%B([0-9]){16}\^[A-Z]{2,26}\/[A-Z]\^([0-9]){7}([A-Z])*\?\;*", cardReaderInput):
        print("Reenter Card Info")
        return None
    # re.split('%B([0-9]{,19})\^[[:alpha:]]{2,26}\/[[:alpha:]]\^[[:alnum:]]*?;*', x))
    cardInfo = re.compile('([A-Z]+)').split(cardReaderInput)
    lastName = cardInfo[3]
    firstInitial = cardInfo[5]
    uniquename = cardInfo[7]
    return lastName, firstInitial, uniquename
    
#description:   Append list of inforamtion to csvfile
#input:         list, string name of CSV file to append to
def writeToCSV(info, csvFile):
    with open(csvFile, mode='a') as file:
        file = csv.writer(file, delimiter=',')
        file.writerow(info)


# x = input()
x = getpass(prompt='')
while(x != quit):
    info = parseCardInfo(x)
    print(info)
    print(infoFill.getUniqnameInfo(info[-1]))
    writeToCSV(info, "signups.csv")
    # x = input()
    x = getpass(prompt='')