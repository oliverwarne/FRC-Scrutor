__name__ = "listcreate"
### FILE LOADING STUFF BEGIN ###

def GetNameAndTeamNum(Scouted_Array):
    return str(Scouted_Array[0]) + ":" + str(Scouted_Array[1]) + ".txt"

def WriteArrayToText(Scouted_Array):
    filename = GetNameAndTeamNum(Scouted_Array)
    f = open(filename,'w')
    f.write(Scouted_Array)
    f.close

    
### FILE LOADING STUFF END ###
