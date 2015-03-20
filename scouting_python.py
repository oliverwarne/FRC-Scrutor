import pickle
__name__ = "main"


"""
Most of the functions return a bool value. The "large" function is going to check which conditionals must be met, and then 
figures out which one  
Data should be parsed as: ["TEAM #","Team Name",INT:Totes stacked reliably,INT:On how many totes can they stack a bin reliably,
BOOL:Can they place a litter in the bin?,BOOL: Do they use the chute?,INT:Match #]
### EXAMPLE ###
["5431","Titan Robotics",6,0,False,True,30]
["TeamNum","TeamName",Totes,BinOnTotes,Litter,Chute,MatchNum]
"""
### CUSTOMIZATION BEGIN ###

# Miniumum of stuff
MinTotes = 0
MinBins = 4

# Bools for checking
MinTotesBool = True
MinBinsOnToteBool = True
NeedsLitter = True
RankedHigherBool = True
MinimumScoreBool = False

# Testing stuff
Titan_Array = ["5431","Titan Robotics",6,0,False,True,30]
GlobalArrayName = [" "]
NewArray = [0,0,0,0,0,0,0]
NewArray2 = []

### CUSTOMIZATION END ###

### LIST MANAGMENT BEGIN ###

def Create0InitArray():
    EmptyArray = []
    for i in range(0,7):
        EmptyArray.append(0)
    return EmptyArray

def InputListIntoScoutedArray(TeamNum,TeamName,Totes,BinOnTotes,Litter,Chute,MatchNum,Scouted_Array):
    InputArray = [TeamNum,TeamName,Totes,BinOnTotes,Litter,Chute,MatchNum]
    for i in InputArray:
        if InputArray.index(i) <= 1: # 2 is the current # of string inputs in the array. I'm so sorry
            if InputArray[0]:
                ParseStringInput(TeamNum,Scouted_Array,"TeamNum")
            if InputArray[1]:
                ParseStringInput(TeamName,Scouted_Array,"TeamName")
        if InputArray.index(i) > 1:
            if InputArray[2]:
                ParseIntegerInput(Totes,Scouted_Array,"Totes")
            if InputArray[3]:
                ParseIntegerInput(BinOnTotes,Scouted_Array,"BinOnTotes")
            if InputArray[4]:
                ParseBoolInput(Litter,Scouted_Array,"Litter")
            if InputArray[5]:
                ParseBoolInput(Chute,Scouted_Array,"Chute")
            if InputArray[6]:
                ParseIntegerInput(MatchNum,Scouted_Array,"MatchNum")
    return Scouted_Array


def ParseStringInput(TeamString,Scouted_Array,DataType):
    # Clean the string input, assign it to a variable, insert it into the list. NOT ABSOLUTE
    ### THIS NEEDS TO BE PUT IN THE REAL ORDER!!!! IT WILL BREAK IF ITS NOT!
    DataType = ParseDataType(DataType)
    if isinstance(TeamString,str):
        Scouted_Array[DataType] = TeamString
    else:
        try:
            TeamString = str(TeamString)
            Scouted_Array[DataType] = TeamString
        except Exception:
            print "Parse string error"
    return Scouted_Array
        
def ParseBoolInput(TeamBool,Scouted_Array,DataType):
    # Clean the string input, assign it to a variable, insert it into the list. NOT ABSOLUTE
    ### THIS NEEDS TO BE PUT IN THE REAL ORDER!!!! IT WILL BREAK IF ITS NOT!
    DataType = ParseDataType(DataType)
    if isinstance(TeamBool,bool):
        Scouted_Array[DataType] = TeamBool
    else:
        try:
            TeamBool = bool(TeamBool)
            Scouted_Array[DataType] = TeamBool
        except Exception:
            print "Parse Bool Error"
    return Scouted_Array
            
def ParseIntegerInput(TeamInt,Scouted_Array,DataType):
    # TeamInt is any number that needs to parsed and put into the list.
    # This snippet actually inserts the TeamInt at the DataType index pos.
    # Datatype is, in reality, the index position of list. Should be passed to
    # this function via the ParseDataType function
    DataType = ParseDataType(DataType)
    if isinstance(TeamInt,int):
        Scouted_Array[DataType] = TeamInt
    return Scouted_Array            

"""
["TeamNum","TeamName",Totes,BinOnTotes,Litter,Chute,MatchNum]
"""

# To pickle a new list (team), use 
# ParseIntegerInput(IntYouWantIn,ArrayYouWantToPutItIn,ParseDataType(TypeOfData))

def ParseDataType(DataType):
    # This snippet parses the datatype that you want in order to set the index 
    # at a position
    if DataType == "TeamNum":
        DataType = 0
    elif DataType == "TeamName":
        DataType = 1
    elif DataType == "Totes":
        DataType = 2
    elif DataType == "BinOnTotes":
        DataType = 3
    elif DataType == "Litter":
        DataType = 4
    elif DataType == "Chute":
        DataType = 5
    elif DataType == "MatchNum":
        DataType = 6
    else:
        print "DataType not recognized! Complain to Oliver"
    return DataType



    
def PeekArray(Scouted_Array,Data):
    TeamNum = Scouted_Array[0]
    TeamName = Scouted_Array[1]
    TeamTotesStacked = Scouted_Array[2]
    TeamBinOnTotes = Scouted_Array[3]
    TeamLitter = Scouted_Array[4]
    TeamChute = Scouted_Array[5]
    TeamMatchNum = Scouted_Array[6]
    
    if Data == "TeamNum":
        return TeamNum
    elif Data == "TeamName":
        return TeamName
    elif Data == "TeamTotesStacked":
        return TeamTotesStacked
    elif Data == "TeamBinOnTotes":
        return TeamBinOnTotes
    elif Data == "TeamBinOnTotes":
        return TeamBinOnTotes
    elif Data == "TeamLitter":
        return TeamLitter
    elif Data == "TeamChute":
        return TeamChute
    elif Data == "TeamMatchNum":
        return TeamMatchNum
    else:
        # TODO : Error raising and handeling
        print "Wrong input!"


### LIST MANAGMENT END ###

### SCOUTED TEAM CHECKING STUFF BEGIN ###

def CheckTotesMin(MinTotesBool,MinTotes,TotesStacked):
    if MinTotesBool:
        if MinTotes >= TotesStacked:
            return True
        elif MinTotes < TotesStacked:
            return False
        else:
            raise NameError("!")
    else:
        return True
   

def CheckBinsMin(MinBinsOnToteBool,MinBins,BinOnTotesStacked):
    if MinBinsOnToteBool:
        if MinBins <= BinOnTotesStacked:
            return True
        elif MinBins > BinOnTotesStacked:
            return False
        else:
            raise NameError("BinOnTotesStacked is too low!")
    else:
        return True
        

def CheckLitter(NeedsLitter,LitterPlaced):
    if NeedsLitter == LitterPlaced:
        return True
    if LitterPlaced == True and NeedsLitter == False:
        return True
    else:
        return False
        
def CheckRankedHigherABS(RankedHigherBool,RankedHigher):
    if RankedHigherBool == RankedHigher:
        return True
    if RankedHigher == True and RankedHigherBool == False:
        return True
    else:
        return False

def CheckRankedHigherData(RankedHigherBool,OurRank,ScoutedRank):
    if RankedHigherBool:
        if OurRank < ScoutedRank:
            return True
        elif OurRank > ScoutedRank:
            return False
        else:
            raise NameError("!")
    else: 
        return True
        
def CheckMinimumScore(MinimumScoreBool,MinimumScore,ScoutedScore):
    if MinimumScoreBool:
        if MinimumScore > ScoutedScore:
            return False
        elif MinimumScore <= ScoutedScore:
            True
    else:
         return True

### SCOUTED TEAM CHECKING STUFF END ###

### FILE LOADING STUFF BEGIN ###

def GetNameAndTeamNum(Scouted_Array):
    return Scouted_Array[0] + " : " + Scouted_Array[1] + ".p"
    
### FILE LOADING STUFF END ###

def BIGFUNCTION(TeamNum,TeamName,TotesStacked,BinOnStacks,LitterInBin,ChuteUsed,MatchNum):
    if CheckTotesMin(True,1,1):
        print "hello"
        

