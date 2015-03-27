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
    if config.MinTotes <= TotesStacked:
        return True
    elif config.MinTotes > TotesStacked:
        return False
    else:
        return True
   
def CheckBinsMin(BinOnTotesStacked):
    if config.MinBins <= BinOnTotesStacked:
        return True
    elif config.MinBins > BinOnTotesStacked:
        return False
    else:
        return True
        
def CheckLitter(LitterPlaced):
    if LitterPlaced:
        return True
    else:
        return False
        
def CheckChute(ChuteUsed):
    if ChuteUsed:
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
        
def CheckMinScore(MinScore,ScoutedScore):
    if config.MinScore:
        if MinScore > ScoutedScore:
            return False
        elif MinScore <= ScoutedScore:
            True
    else:
         return True

### SCOUTED TEAM CHECKING STUFF END ###


