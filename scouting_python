import pickle

"""
Most of the functions return a bool value. The "large" function is going to check which conditionals must be met, and then 
figures out which one  
Data should be parsed as: ["TEAM #","Team Name",INT:Totes stacked reliably,INT:On how many totes can they stack a bin reliably,
BOOL:Can they place a litter in the bin?,BOOL: Do they use the chute?,INT:Match #]
### EXAMPLE ###
["5431","Titan Robotics",6,0,False,True,30]
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

### CUSTOMIZATION END ###

### LIST MANAGMENT BEGIN ###

def PopArray(Scouted_Array,Data):
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



def ParseNum(TeamNum):
    # Clean the totes input, assign it to a variable, insert it into the list
    try:
        # TODO: write code...
        x = int(TeamNum)
    except Exception, e:
        raise SystemExit

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

### SCOUTED TEAM TESTING STUFF END ###

### FILE LOADING STUFF BEGIN ###

def GetNameAndTeamNum(Scouted_Array):
    return Scouted_Array[0] + " : " + Scouted_Array[1]
    
### FILE LOADING STUFF END ###

def BIGFUNCTION(TeamNum,TeamName,TotesStacked,BinOnStacks,LitterInBin,ChuteUsed,MatchNum):
    if CheckTotesMin(True,1,1):
        print "hello"
        

