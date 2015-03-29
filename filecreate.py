### FILE LOADING STUFF BEGIN ###
def GetNameAndTeamNum(Scouted_Array):
    return str(Scouted_Array[0]) + "-" + str(Scouted_Array[1]) + "-" + str(Scouted_Array[6]) + ".txt"

def WriteArrayToText(Scouted_Array):
    filename = GetNameAndTeamNum(Scouted_Array)
    f = open(filename,'w')
    f.write(str(Scouted_Array))
### FILE LOADING STUFF END ###