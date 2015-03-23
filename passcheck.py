
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

### SCOUTED TEAM CHECKING STUFF BEGIN ###

def CheckTotesMin(MinTotesBool,MinTotes,TotesStacked):
    if MinTotesBool == True:
        if MinTotes <= TotesStacked:
            return True
        elif MinTotes > TotesStacked:
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
        
def CheckChute(ChuteBool,ChuteUsed):
    if ChuteBool == ChuteUsed:
        return True
    elif ChuteUsed == True and ChuteBool == False:
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


