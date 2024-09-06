import json


# Function to generate the rank of the faulty statment
def gen_rank(method,faultyLine,outputFile,suspiciousness):
    d = {}
    for i in range(0,len(suspiciousness)):
        key = float(suspiciousness[i])
        #print key
        if key not in d:
            d[key] = []
        d[key].append(i)

    not_faulty=0
    worstcase_mid=0
    bestcase=0
    flag=0
    faultyLine1= int(faultyLine)-1

    for x in sorted(d):
       # print(d, len(d[x]))
        if faultyLine1 not in d[x] and flag==0:
            not_faulty=not_faulty+len(d[x])
        elif faultyLine1 not in d[x] and flag==1:
            bestcase=bestcase+len(d[x])
        else: 
            flag=1
            worstcase_mid=len(d[x])
    print("The Best rank and Worst rank generated for the  faulty line "+str(faultyLine)+" using "+method+" is " +str(bestcase+1)+" to "+str(bestcase+worstcase_mid)+".") 
    worstcase=bestcase+worstcase_mid
    writeData(method, faultyLine, outputFile, bestcase+1, worstcase)



def writeData(method, faultyLine, outputFile, bestcase, worstcase):
    Info = {
    'Method Name' : method,  
    'Faulty Line' : faultyLine,
    'Best Case Rank': bestcase,
    'Worst Case Rank': worstcase,
    }
    with open(outputFile+".json", "w") as data:
        data.write(json.dumps(Info))
        data.close()