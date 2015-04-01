### FILE LOADING STUFF BEGIN ###
def GetNameAndTeamNum(Scouted_Array): #returns the filename for scan.py
    return str(Scouted_Array[0]) + "-" + str(Scouted_Array[1]) + "-" + str(Scouted_Array[6]) + ".txt"

def WriteArrayToText(Scouted_Array): # a kind of broken function that can't be used anywhere except
                                     # for our very specific usage case inside scan.py
    f = open(GetNameAndTeamNum(Scouted_Array),'w')
    f.write(str(Scouted_Array))
    f.close
### FILE LOADING STUFF END ###