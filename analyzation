import passcheck

# General overview. This module should accept a filled array, then fill another 
# array (of the 5 things it checks for), with True/False based on if it passes
# the checks from passcheck or not.

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

# TODO : This is moderately hacky. I need to get into classes.
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

def InitalizeEmptyBoolArray():
    NewArray = []
    NewArray.append(0) * 5
    return NewArray


def CreateBoolArray(EmptyBoolArray,FilledArray):
    # TODO : Figure out what the heck i was trying to do while operating on 5
    # hours of sleep. Future me. I'm sorry. This relates to scoring but my
    # brain is impolding. 
    #Assigned integer positions inside of the old array
    TotesStackedInt = FilledArray[2]
    BinOnTotesInt = FilledArray[3]
    Litter = FilledArray[4]
    Chute = FilledArray[5]
    
    #Assigns bool position inside the new array
    TotesStackedBool = EmptyBoolArray[0]
    BinOnTotesBool = EmptyBoolArray[1]
    LitterBool = EmptyBoolArray[2]
    ChuteBool = EmptyBoolArray[3]
    
