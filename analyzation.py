import passcheck

# General overview. This module should accept a filled array, then fill another 
# array (of the 5 things it checks for), with True/False based on if it passes
# the checks from passcheck or not.

### CUSTOMIZATION BEGIN ###

# TODO : Stick this in a config file

# Miniumum of stuff
global MinTotes
MinTotes = 1
global MinBins
MinBins = 1

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
TotesValue = 2
BinValue = 1
LitterValue = 1
ChuteValue = 1

# Absolute Needs
global ABSTotesPass,ABSBinPass,ABSLitterPass,ABSChutePass
ABSTotesPass = True
ABSBinPass = True
ABSLitterPass = True
ABSChutePass = True

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
    # Creates an array that is filled with 0's, to be filled with boolean statements
    NewArray = []
    for num in range(0,5):
        NewArray.append(0) 
    return NewArray

def CreateBoolArray(FilledArray):
    # FilledArray is an array that's filled with proper data. It turns it into a boolean
    # from the passcheck module
    
    #Assigned integer positions inside of the old array
    TotesStackedInt = FilledArray[2]
    BinOnTotesInt = FilledArray[3]
    Litter = FilledArray[4]
    Chute = FilledArray[5]
    # It should be [Does have enough totes stacked, Does stack a bin on enough totes, does throw litter, does use chute]
    EmptyBoolArray = InitalizeEmptyBoolArray()
    EmptyBoolArray[0] = passcheck.CheckTotesMin(MinTotesBool,MinTotes,TotesStackedInt)
    EmptyBoolArray[1] = passcheck.CheckBinsMin(MinBinsOnToteBool,MinBins,BinOnTotesInt)
    EmptyBoolArray[2] = passcheck.CheckLitter(NeedsLitter,Litter)
    EmptyBoolArray[3] = passcheck.CheckChute(ChuteBool,Chute)
    return EmptyBoolArray

def BoolArrayIntoTeamScore(BoolArray):
    # This function accepts the BoolArray, and calculate the score by 
    # multiplying the global value by the Bool which is turned into 
    # 1's and 0's by the multiplying operator. It is a float to accommodate
    # non-whole numbers
    BoolArray[0] = BoolArray[0] * float(TotesValue)
    BoolArray[1] = BoolArray[1] * float(BinValue)
    BoolArray[2] = BoolArray[2] * float(LitterValue)
    BoolArray[3] = BoolArray[3] * float(ChuteValue) 
    TeamScore = sum(BoolArray)
    return TeamScore

def ReturnTeamScorePercentage(TeamScore):
    # Turns the team score into a percentage via creating a proportion from
    # the maximum possible score and the score received. 
    # MaxTotalScore is the sum of the maximum values.
    MaxTotalScore = TotesValue + BinValue + LitterValue + ChuteValue
    PercentagePropotion = float(TeamScore) / float(MaxTotalScore)
    Percentage = PercentagePropotion * 100
    return Percentage

def PercentageCheckAbsolute(FilledArray):
    BoolArray = CreateBoolArray(FilledArray)
    TeamScore = BoolArrayIntoTeamScore(BoolArray)
    # The ABS_____ are the global variables. If it is true, then check if the relevant
    # index on the array is true. If it is, then it calculates the team score. If it
    # is false, then it sets percentage at 0.
    # If none of the "must haves" are true, then it setss p
    if ABSTotesPass:
        if BoolArray[0]:
            Percentage = ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if ABSBinPass:
        if BoolArray[1]:
            Percentage = ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if ABSLitterPass:
        if BoolArray[2]:
            Percentage = ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if ABSChutePass:
        if BoolArray[3]:
            Percentage = ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if not ABSTotesPass and not ABSBinPass and not ABSLitterPass and not ABSChutePass:
        Percentage = ReturnTeamScorePercentage(TeamScore)
    return Percentage