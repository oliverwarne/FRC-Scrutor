import listcreate
import listinterp
import analyzation
import config

def Create0InitalizedArray():
    EmptyArray = []
    for n in range(0,7):
        EmptyArray.append(0)
    return EmptyArray
    
EmptyArray = Create0InitalizedArray()
EmptyArray2 = Create0InitalizedArray()

BoolArrayTrue = [True,True,True,True]
BoolArrayFalse = [False,False,False,False]
BoolArrayTrueThenFalse = [True,False,False,False]
BoolArrayFalseThenTrue = [False,True,True,True] 

### LIST CREATE TESTS ###
print "LIST CREATE"
print EmptyArray
listcreate.InputListIntoScoutedArray("5431","Titan Robotics",6,0,False,True,30,EmptyArray)
# Should return ["5431","Titan Robotics",6,0,False,True,30,EmptyArray]
print EmptyArray

#### LIST INTERP TEST ###
print "LIST INTERP"
print listinterp.PeekArrayTest(EmptyArray,"TeamChute")
# Should return True
print listinterp.PeekArrayTest(EmptyArray2,"TeamChute")
# Should return 0

### ANALYZATION TESTS ###
print "ANALYZATION"
print analyzation.PercentageCheckAbsolute(EmptyArray)

def PercentageCheckAbsoluteHacky(BoolArray):
    TeamScore = analyzation.BoolArrayIntoTeamScore(BoolArray)
    # The ABS_____ are the global variables. If it is true, then check if the relevant
    # index on the array is true. If it is, then it calculates the team score. If it
    # is false, then it sets percentage at 0.
    # If none of the "must haves" are true, then it setss p
    if config.ABSTotesPass:
        if BoolArray[0]:
            Percentage = analyzation.ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if config.ABSBinPass and Percentage != 0:
        if BoolArray[1]:
            Percentage = analyzation.ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if config.ABSLitterPass and Percentage != 0:
        if BoolArray[2]:
            Percentage = analyzation.ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if config.ABSChutePass and Percentage != 0:
        if BoolArray[3]:
            Percentage = analyzation.ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if not config.ABSTotesPass and not config.ABSBinPass and not config.ABSLitterPass and not config.ABSChutePass:
        Percentage = analyzation.ReturnTeamScorePercentage(TeamScore)
    return Percentage

# Bool percentage checking

print BoolArrayTrue
print PercentageCheckAbsoluteHacky(BoolArrayTrue)
print BoolArrayFalse
print PercentageCheckAbsoluteHacky(BoolArrayFalse)
print BoolArrayFalseThenTrue
print PercentageCheckAbsoluteHacky(BoolArrayFalseThenTrue)
print BoolArrayTrueThenFalse
print PercentageCheckAbsoluteHacky(BoolArrayTrueThenFalse)



# TODO : Figure out how to write a test for this
