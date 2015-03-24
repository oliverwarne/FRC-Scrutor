__name__ = "listinterp"

def PeekArrayTest(Scouted_Array,Data):
    # You pass this function the 
    IndexDict = {
                'TeamNum':Scouted_Array[0],
                'TeamName':Scouted_Array[1],
                'TeamTotesStacked':Scouted_Array[2],
                'TeamBinOnTotes':Scouted_Array[3],
                'TeamLitter':Scouted_Array[4],
                'TeamChute':Scouted_Array[5],
                'TeamMatchNum':Scouted_Array[6]
                }
    
    return IndexDict[Data]

