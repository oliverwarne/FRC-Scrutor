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


# Testing stuff
Titan_Array = ["5431","Titan Robotics",6,0,False,True,30]
GlobalArrayName = [" "]
NewArray = [0,0,0,0,0,0,0]
NewArray2 = []
NewBoolArray = [0,0,0,0]

### CUSTOMIZATION END ###

def InitalizeEmptyBoolArray():
    NewArray = []
    NewArray.append(0) * 5
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

print CreateBoolArray(NewBoolArray,Titan_Array)
