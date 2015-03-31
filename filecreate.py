### FILE LOADING STUFF BEGIN ###
def GetNameAndTeamNum(Scouted_Array): #returns the filename for scan.py
    return str(Scouted_Array[0]) + "-" + str(Scouted_Array[1]) + "-" + str(Scouted_Array[6]) + ".txt"

def WriteArrayToText(Scouted_Array): # a kind of broken function that can't be used anywhere except
                                     # for our very specific usage case inside scan.py
    filename = GetNameAndTeamNum(Scouted_Array)
    f = open(filename,'w')
    f.write(str(Scouted_Array))
### FILE LOADING STUFF END ###