import config
from ast import literal_eval

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
    TotesStacked = int(TotesStacked)
    if config.MinTotes <= TotesStacked:
        return True
    elif config.MinTotes > TotesStacked:
        return False
    else:
        return True
   
def CheckBinsMin(BinOnTotesStacked):
    BinOnTotesStacked = int(BinOnTotesStacked)
    if config.MinBins <= BinOnTotesStacked:
        return True
    elif config.MinBins > BinOnTotesStacked:
        return False
    else:
        return True
        
def CheckLitter(LitterPlaced):
    # Yes, I know that I should be using the "pythonic" way, but I am not sure
    # how to use try/except when there is no user input to ask for the user
    # to fix it.
    if not isinstance(LitterPlaced,bool):
        LitterPlaced = literal_eval(LitterPlaced) # oops. hackiness to max
    if LitterPlaced:
        return True
    elif LitterPlaced == False:
        return False
        
def CheckChute(ChuteUsed):
    if not isinstance(ChuteUsed,bool): 
        ChuteUsed = literal_eval(ChuteUsed)
    if ChuteUsed:
        return True
    elif ChuteUsed == False:
        return False

def CheckMinScore(MinScore,ScoutedScore):
    if MinScore > ScoutedScore:
        return False
    elif MinScore <= ScoutedScore:
        True
    else:
        return True



###This is stuff that we are not currently using, but might use in the future###

#def CheckRankedHigherABS(RankedHigher):
#    if config.RankedHigherBool == RankedHigher:
#        return True
#    if RankedHigher and config.RankedHigherBool:
#        return True
#    else:
#       return False

#def CheckRankedHigherData(OurRank,ScoutedRank):
#    if config.RankedHigherBool:
#        if OurRank < ScoutedRank:
#            return True
#        elif OurRank > ScoutedRank:
#            return False
#        else:
#           raise NameError("!")
#    else: 
#        return True
        
### SCOUTED TEAM CHECKING STUFF END ###


