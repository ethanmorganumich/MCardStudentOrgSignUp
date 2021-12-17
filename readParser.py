import re
#%B6008475547260813^MORGAN/E^2412120ETCMO?;6008475547260813=2412120=302135592?
#
#%B6008473657049217^AGRAWAL/R^2305120RAGRAW?;6008473657049217=2305120=439169501?

def parseCardInfo(cardReaderInput):

    #validation regex: 
    if not re.match('%B([0-9]{,19})\^[[:alpha:]]{2,26}\/[[:alpha:]]\^[[:alnum:]]*?;*', cardReaderInput):
        print("Reenter Card Info")
        return None
    # re.split('%B([0-9]{,19})\^[[:alpha:]]{2,26}\/[[:alpha:]]\^[[:alnum:]]*?;*', x))
    cardInfo = re.split('(\W)', cardReaderInput)
    cardNum = cardInfo[2][1:]
    lastName = cardInfo[4]
    firstInital = cardInfo[6]
    uniquename = cardInfo[8][7:]
    return uniquename
    



# parseCardInfo('%B6008475547260813^MORGAN/E^2412120ETCMO?;6008475547260813=2412120=302135592?')
x = input()
while(x != quit):
    print(parseCardInfo(x))
    x = input()
