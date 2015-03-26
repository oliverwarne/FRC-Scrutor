import config

######
#Most of the functions return a bool value. 
#
#Data should be parsed as: ["TEAM #","Team Name",INT:Totes stacked reliably,INT:On how many totes can they stack a bin reliably,
#BOOL:Can they place a litter in the bin?,BOOL: Do they use the chute?,INT:Match #]
### EXAMPLE ###
#["5431","Titan Robotics",6,0,False,True,30]
#["TeamNum","TeamName",Totes,BinOnTotes,Litter,Chute,MatchNum]
######

### SCOUTED TEAM CHECKING STUFF BEGIN ###

def CheckTotesMin(TotesStacked):
    if config.MinTotesBool:
        if config.MinTotes <= TotesStacked:
            return True
        elif config.MinTotes > TotesStacked:
            return False
        else:
            raise NameError("!")
    else:
        return True
   
def CheckBinsMin(BinOnTotesStacked):
    if config.MinBinsOnToteBool:
        if config.MinBins <= BinOnTotesStacked:
            return True
        elif config.MinBins > BinOnTotesStacked:
            return False
        else:
            raise NameError("BinOnTotesStacked is too low!")
    else:
        return True
        
def CheckLitter(LitterPlaced):
    if config.NeedsLitter == LitterPlaced:
        return True
    if LitterPlaced == True and config.NeedsLitter == False:
        return True
    else:
        return False
        
def CheckChute(ChuteUsed):
    if config.ChuteBool == ChuteUsed:
        return True
    elif ChuteUsed == True and config.ChuteBool == False:
        return True
    else:
        return False
        
def CheckRankedHigherABS(RankedHigher):
    if config.RankedHigherBool == RankedHigher:
        return True
    if RankedHigher == True and config.RankedHigherBool == False:
        return True
    else:
        return False

def CheckRankedHigherData(OurRank,ScoutedRank):
    if config.RankedHigherBool:
        if OurRank < ScoutedRank:
            return True
        elif OurRank > ScoutedRank:
            return False
        else:
            raise NameError("!")
    else: 
        return True
        
def CheckMinimumScore(MinimumScore,ScoutedScore):
    if config.MinimumScoreBool:
        if MinimumScore > ScoutedScore:
            return False
        elif MinimumScore <= ScoutedScore:
            True
    else:
         return True

### SCOUTED TEAM CHECKING STUFF END ###


