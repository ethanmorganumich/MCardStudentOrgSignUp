import requests
import json

#description:   get lastname of first name of uniqname
#input:         string of uniqname
#output:        [Lastname, FirstName]
def getUniqnameInfo(uniqname):
    #input check
    #given blank string or something other than a string
    if uniqname == "" or type(uniqname) != type("string"):
        print("input error")
        return -1


    url = "https://mcommunity.umich.edu/mcPeopleService/people/" + uniqname
    response = requests.get(url)

    response = response.json()

    if response["person"]["errors"] != "":
        print("Not found in database:", uniqname)
    
    displayName = response["person"]["displayName"].split()
    return displayName[0], displayName[-1]

