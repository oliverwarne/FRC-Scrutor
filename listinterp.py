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

    if Data == "TeamNum":
        Data = TeamNum
    elif Data == "TeamName":
        Data = TeamName
    elif Data == "TeamTotesStacked":
        Data = TeamTotesStacked
    elif Data == "TeamBinOnTotes":
        Data = TeamBinOnTotes
    elif Data == "TeamLitter":
        Data = TeamLitter
    elif Data == "TeamChute":
        Data = TeamChute
    elif Data == "TeamMatchNum":
        Data = TeamMatchNum
    else:
        # TODO : Error raising and handeling
        print "Wrong input!"
    return Data

def PeekArrayHACK(Scouted_Array,Data):
    # This hack turns the string "False" and "True" into real bools to be passed
    TeamNum = Scouted_Array[0]
    TeamName = Scouted_Array[1]
    TeamTotesStacked = Scouted_Array[2]
    TeamBinOnTotes = Scouted_Array[3]
    TeamLitter = Scouted_Array[4]
    TeamChute = Scouted_Array[5]
    TeamMatchNum = Scouted_Array[6]
    
    if Data == "TeamNum":
        Data = TeamNum
    elif Data == "TeamName":
        Data = TeamName
    elif Data == "TeamTotesStacked":
        Data = TeamTotesStacked
    elif Data == "TeamBinOnTotes":
        Data = TeamBinOnTotes
    elif Data == "TeamLitter":
        Data = bool(TeamLitter)
    elif Data == "TeamChute":
        Data = bool(TeamChute)
    elif Data == "TeamMatchNum":
        Data = TeamMatchNum
    else:
        # TODO : Error raising and handeling
        print "Wrong input!"
    return Data
