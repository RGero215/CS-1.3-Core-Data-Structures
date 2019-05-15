import resource
import platform
"""
You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a
single phone number. How quickly can you find the cost of calling this number?
1)Split the routes into a dictionary for constant time Searching
    -When splitting seperate by comma
    -Check if newValue < oldVal only update if its less
2)Loop through len(phone#)substringing last # off every iteraiton
3)If []results ->helper function to find lowest route cost
#Worked on with Jonathan Kopp
"""
#O(3n) = 0(n)
def splitIntoArray(path, pn):
    with open(path) as file: #0(n)
        lines = file.read().splitlines()
    theRoutes = []
    theCosts = []
    for line in lines: #0(n)
        mylist = line.split(',')
        theRoutes.append(mylist[0])
        theCosts.append(mylist[1])
    ctr = len(pn) - 1
    while(ctr > 1): #0(phoneNumber length)
        s = pn[0:ctr]
        indexes = []
        curIndex = 0
        for route in theRoutes:#0(n)
            if(route == s):
                indexes.append(curIndex)
                print("Found")
            curIndex += 1
        if(len(indexes) > 0):
            lowestCost = 999999
            for i in indexes:#0(number of identical indexes)
                if(float(theCosts[i]) < lowestCost):
                    lowestCost = theCosts[i]
            return lowestCost
        ctr -= 1

if __name__ == '__main__':
    print(splitIntoArray('route-costs-100.txt', '+18017154269'))
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    usage=round(usage/float(1<<20),2)

# print memory usage
    print("Memory Usage: {} mb.".format(usage))