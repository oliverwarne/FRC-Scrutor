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
    # It should be [Does have enough totes stacked, Does stack a bin on enough totes, does throw litter, does use chute]
    EmptyBoolArray[0] = passcheck.CheckTotesMin(MinTotesBool,MinTotes,TotesStackedInt)
    EmptyBoolArray[1] = passcheck.CheckBinsMin(MinBinsOnToteBool,MinBins,BinOnTotesInt)
    EmptyBoolArray[2] = passcheck.CheckLitter(NeedsLitter,Litter)
    EmptyBoolArray[3] = passcheck.CheckChute(ChuteBool,Chute)
    return EmptyBoolArray

def BoolArrayIntoTeamScore(BoolArray):
    BoolArray[0] = BoolArray[0] * float(TotesValue)
    BoolArray[1] = BoolArray[1] * float(BinValue)
    BoolArray[2] = BoolArray[2] * float(LitterValue)
    BoolArray[3] = BoolArray[3] * float(ChuteValue) 
    TeamScore = sum(BoolArray)
    return TeamScore

def ReturnTeamScorePercentage(TeamScore):
    ScoreList = [TotesValue,BinValue,LitterValue,ChuteValue]
    MaxTotalScore = sum(ScoreList)
    PercentagePropotion = float(TeamScore) / float(MaxTotalScore)
    Percentage = PercentagePropotion * 100
    return Percentage

# TODO : Figure out why the heck this breaks if you call it twice. has to be
# something to do with global variables. but what?

def PercentageCheckAbsolute(BoolArray):
    TeamScore = BoolArrayIntoTeamScore(BoolArray)
    if ABSTotesPass:
        if BoolArray[0]:
            ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if ABSBinPass:
        if BoolArray[1]:
            ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if ABSLitterPass:
        if BoolArray[2]:
            ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if ABSChutePass:
        if BoolArray[3]:
            ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    Percentage = ReturnTeamScorePercentage(TeamScore)
    return Percentage

