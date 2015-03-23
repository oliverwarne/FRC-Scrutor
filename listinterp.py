__name__ = "listinterp"


def PeekArray(Scouted_Array,Data):
    # You pass this function the 
    TeamNum = Scouted_Array[0]
    TeamName = Scouted_Array[1]
    TeamTotesStacked = Scouted_Array[2]
    TeamBinOnTotes = Scouted_Array[3]
    TeamLitter = Scouted_Array[4]
    TeamChute = Scouted_Array[5]
    TeamMatchNum = Scouted_Array[6]

    IndexDict = {
                'TeamNum':TeamNum,
                'TeamName':TeamName,
                'TeamTotesStacked':TeamTotesStacked,
                'TeamBinOnTotes':TeamBinOnTotes,
                'TeamLitter':TeamLitter,
                'TeamChute':TeamChute,
                'TeamMatchNum':TeamMatchNum
                }
    
    return IndexDict[Data]

def PeekArrayHACK(Scouted_Array,Data):
    # This hack turns the string "False" and "True" into real bools to be passed
    TeamNum = Scouted_Array[0]
    TeamName = Scouted_Array[1]
    TeamTotesStacked = Scouted_Array[2]
    TeamBinOnTotes = Scouted_Array[3]
    TeamLitter = bool(Scouted_Array[4])
    TeamChute = bool(Scouted_Array[5])
    TeamMatchNum = Scouted_Array[6]
    
    IndexDict = {
                'TeamNum':TeamNum,
                'TeamName':TeamName,
                'TeamTotesStacked':TeamTotesStacked,
                'TeamBinOnTotes':TeamBinOnTotes,
                'TeamLitter':TeamLitter,
                'TeamChute':TeamChute,
                'TeamMatchNum':TeamMatchNum
                }
    
    return IndexDict[Data]
