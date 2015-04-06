import passcheck
import config
from glob import glob

# General overview. This module should accept a filled array, then fill another 
# array (of the 5 things it checks for), with True/False based on if it passes
# the checks from passcheck or not.

def CreateBoolArray(scouted_Array):
    boolArray = []
    boolArray.append(passcheck.CheckTotesMin(scouted_Array[2]))
    boolArray.append(passcheck.CheckBinsMin(scouted_Array[3]))
    boolArray.append(passcheck.CheckLitter(scouted_Array[4]))
    boolArray.append(passcheck.CheckChute(scouted_Array[5]))
    return boolArray

def BoolArrayIntoTeamScore(boolArray):
    scoreArray = [config.TotesValue,config.BinValue,config.LitterValue,config.ChuteValue]
    for i in boolArray:
        index = boolArray.index(i)
        boolArray[index] *= scoreArray[index]
    return sum(boolArray)

def ReturnTeamScorePercentage(teamScore):
    maximumScore = float(config.TotesValue) + float(config.BinValue) + float(config.LitterValue) + float(config.ChuteValue)
    percentage = teamScore / maximumScore * 100
    return percentage




def PercentageCheckAbsolute(FilledArray):
    BoolArray = CreateBoolArray(FilledArray)
    TeamScore = BoolArrayIntoTeamScore(BoolArray)
    # The ABS_____ are the global variables. If it is true, then check if the relevant
    # index on the array is true. If it is, then it calculates the team score. If it
    # is false, then it sets percentage at 0.
    # If none of the "must haves" are true, then it setss p
    if config.ShouldCheckTotes:
        if BoolArray[0]:
            Percentage = ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if config.ShouldCheckBin and Percentage != 0:
        if BoolArray[1]:
            Percentage = ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if config.ShouldCheckLitter and Percentage != 0:
        if BoolArray[2]:
            Percentage = ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if config.ShouldCheckChute and Percentage != 0:
        if BoolArray[3]:
            Percentage = ReturnTeamScorePercentage(TeamScore)
        else:
            Percentage = 0
    if not config.ShouldCheckTotes and not config.ShouldCheckBin and not config.ShouldCheckLitter and not config.ShouldCheckChute:
        Percentage = ReturnTeamScorePercentage(TeamScore)
    return Percentage