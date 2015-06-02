from ast import literal_eval
import config

class team():

    def __init__(self, TeamList):
        #assert TeamList is list
        self.TeamNum = TeamList[0]
        self.TeamName = TeamList[1]
        self.MatchNum = TeamList[5]
        self.Notes = TeamList[9]

        self.StackedHeight = literal_eval(TeamList[2])
        self.BinStackedHeight = literal_eval(TeamList[3])
        self.ChuteUsed = literal_eval(TeamList[6])
        self.BrokenBot = literal_eval(TeamList[12])
        self.AlternatePlatform = literal_eval(TeamList[7])
        self.StealBins = literal_eval(TeamList[8])
        self.ThrowNoodles = literal_eval(TeamList[10])
        self.FillBin = literal_eval(TeamList[11])
        self.Coopertition = literal_eval(TeamList[11])
        #  self.OtherToteHeightBin = literal_eval(TeamList[12])
        self.Autonomous = literal_eval(TeamList[13])

    def TeamIdentity(self):
        TeamIdentity = self.TeamName + " " + self.TeamNum #gets team name + num
        return TeamIdentity

    def boolPassFail(self,shouldCheck,checkBool):
        if shouldCheck and checkBool:
            return True
        elif not shouldCheck and checkBool:
            return True
        elif shouldCheck == checkBool:
            return True
        else:
            return False

    def MatchPercentage(self):
        PercentageArray = [0, 0, 0, 0, 0, 0, 0, 0]

        if self.BrokenBot or self.BinStackedHeight < config.MinimumBinHeight and config.absBin or self.AlternatePlatform:
            percentage = 0
        else:
            PercentageArray[0] = self.StackedHeight >= config.heightMin * config.heightValue
            PercentageArray[1] = self.BinStackedHeight >= config.binMin * config.binValue
            #  PercentageArray[2] = (team[5] >= config.stacksMin * config.stacksValue
            PercentageArray[2] = self.Autonomous * config.autonValue
            PercentageArray[4] = team.boolPassFail(self,config.bankrobCheck, self.StealBins) * config.bankrobValue
            PercentageArray[5] = config.throwNoodleValue
            #PercentageArray[5] = Team.boolPassFail(self,config.throwNoodleCheck, self.ThrowNoodles) * config.throwNoodleValue
            PercentageArray[6] = team.boolPassFail(self,config.noodleInBinCheck, self.FillBin) * config.noodleInBinValue
            PercentageArray[7] = self.ChuteUsed * config.chuteValue

            teamScore = sum(PercentageArray)
            maxScore = config.heightValue + config.binValue + config.stacksValue + config.litterValue + config.bankrobValue
            percentage = float(teamScore) / float(maxScore) * 100
        return percentage

    def main(self):
        testList = ['71','Hammon','2','2','False','7','False','False','True','','False','False','False','False']

        testObj = team(testList)
        print testObj.TeamIdentity()
        print testObj.MatchPercentage()

        return percentage
if __name__ == '__main__':
    team.main()