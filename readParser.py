import re
import csv
#%B6008475547260813^MORGAN/E^2412120ETCMO?;6008475547260813=2412120=302135592?
#Card Num          ^ LastName/First inital^ num+uniquname?;
#%B6008473657049217^AGRAWAL/R^2305120RAGRAW?;6008473657049217=2305120=439169501?
#%B6008473507106514^ZOU/H^2608120TINAZOU?;6008473507106514=2608120=349611241?


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
    

def writeToCSV(info):
    with open("signups.csv", mode='a') as signups:
        signups = csv.writer(signups, delimiter=',')
        signups.writerow(info)


# print(parseCardInfo('%B6008475547260813^MORGAN/E^2412120ETCMO?;6008475547260813=2412120=302135592?'))
x = input()
while(x != quit):
    info = parseCardInfo(x)
    print(info)
    writeToCSV(info)
    x = input()
