import passcheck

# General overview. This module should accept a filled array, then fill another 
# array (of the 5 things it checks for), with True/False based on if it passes
# the checks from passcheck or not.

### CUSTOMIZATION BEGIN ###

# Miniumum of stuff
global MinTotes
MinTotes = 1
global MinBins
MinBins = 4

# Bools for checking
global MinTotesBool
MinTotesBool = True
global MinBinsOnToteBool
MinBinsOnToteBool = True
global NeedsLitter
NeedsLitter = True
global RankedHigherBool
RankedHigherBool = True
global MinimumScoreBool
MinimumScoreBool = False
global ChuteBool
ChuteBool = True

# Scoring stuff
global TotesValue,BinValue,LitterValue,ChuteValue
TotesValue = 3
BinValue = 1
LitterValue = 1
ChuteValue = 1

# Absolute Needs
global ABSTotesPass,ABSBinPass,ABSLitterPass,ABSChutePass
ABSTotesPass = True
ABSBinPass = True
ABSLitterPass = True
ABSChutePass = False

# Testing stuff
Titan_Array = ["5431","Titan Robotics",6,0,False,True,30]
GlobalArrayName = [" "]
NewArray = [0,0,0,0,0,0,0]
NewArray2 = []
NewBoolArray = [0,0,0,0]
FilledBoolArray = [True,False,True,False]
FilledBoolArrayTrue = [True,True,True,True]

### CUSTOMIZATION END ###

def InitalizeEmptyBoolArray():
    NewArray = []
    NewArray.append(0) * 3
    return NewArray


def CreateBoolArray(EmptyBoolArray,FilledArray):
    #Assigned integer positions inside of the old array
    TotesStackedInt = FilledArray[2]
    BinOnTotesInt = FilledArray[3]
    Litter = FilledArray[4]
    Chute = FilledArray[5]
    
    #Assigns bool position inside the new array
    
    
    # It should be [Does have enough totes stacked, Does stack a bin on enough totes, does throw litter, does use chute]
    
    EmptyBoolArray[0] = passcheck.CheckTotesMin(MinTotesBool,MinTotes,TotesStackedInt)
    EmptyBoolArray[1] = passcheck.CheckBinsMin(MinBinsOnToteBool,MinBins,BinOnTotesInt)
    EmptyBoolArray[2] = passcheck.CheckLitter(NeedsLitter,Litter)
    EmptyBoolArray[3] = passcheck.CheckChute(ChuteBool,Chute)
    return EmptyBoolArray

def BoolArrayIntoTeamScore(BoolArray):
    BoolArray[0] = BoolArray[0] * TotesValue
    BoolArray[1] = BoolArray[1] * BinValue
    BoolArray[2] = BoolArray[2] * LitterValue
    BoolArray[3] = BoolArray[3] * ChuteValue 
    TeamScore = sum(BoolArray)
    print "The teamscore is" 
    print TeamScore
    print BoolArray[0]
    return TeamScore

def BoolArrayIntoTeamScoreLoop(BoolArray):
    for i in BoolArray:
        z

print BoolArrayIntoTeamScore(FilledBoolArrayTrue)

def ReturnTeamScorePercentage(TeamScore):
    ScoreList = [TotesValue,BinValue,LitterValue,ChuteValue]
    MaxTotalScore = sum(ScoreList)
    PercentagePropotion = float(TeamScore) / float(MaxTotalScore)
    Percentage = PercentagePropotion * 100
    return Percentage

print ReturnTeamScorePercentage(BoolArrayIntoTeamScore(FilledBoolArrayTrue))

def PercentageCheckAbsolute(BoolArray):
    TeamScore = BoolArrayIntoTeamScore(BoolArray)
    if ABSTotesPass == True:
        if BoolArray[0] == True:
            ReturnTeamScorePercentage(TeamScore)
        elif BoolArray[0] == False:
            Percentage = 0
    if ABSBinPass == True:
        if BoolArray[1] == True:
            ReturnTeamScorePercentage(TeamScore)
        elif BoolArray[1] == False:
            Percentage = 0
    if ABSLitterPass == True:
        if BoolArray[2] == True:
            ReturnTeamScorePercentage(TeamScore)
        elif BoolArray[2] == False:
            Percentage = 0
    if ABSChutePass == True:
        if BoolArray[3] == True:
            ReturnTeamScorePercentage(TeamScore)
        elif BoolArray[3] == False:
            Percentage = 0
    else:
        Percentage = ReturnTeamScorePercentage(TeamScore)
    return Percentage
    
print PercentageCheckAbsolute(FilledBoolArrayTrue)
print PercentageCheckAbsolute(FilledBoolArray)
