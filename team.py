from ast import literal_eval
import config


class Team():

    def __init__(self, TeamList):
        assert isinstance(TeamList,list)
        #  Team identification
        self.TeamNum = TeamList[0]
        self.TeamName = TeamList[1]
        self.MatchNum = TeamList[2]
        self.Notes = TeamList[3]
        #  Team data
        self.StackedHeight = literal_eval(TeamList[4])
        self.BinStackedHeight = literal_eval(TeamList[5])
        self.ChuteUsed = literal_eval(TeamList[6])
        self.BrokenBot = literal_eval(TeamList[7])
        self.AlternatePlatform = literal_eval(TeamList[8])
        self.StealBins = literal_eval(TeamList[9])
        self.ThrowNoodles = literal_eval(TeamList[10])
        self.FillBin = literal_eval(TeamList[11])
        self.Coopertition = literal_eval(TeamList[12])
        self.OtherToteHeightBin = literal_eval(TeamList[13])
        self.Autonomous = literal_eval(TeamList[14])
        self.ToteSet = literal_eval(TeamList[15])

    def TeamIdentity(self):
        TeamIdentity = self.TeamName + " " + self.TeamNum #gets team name + num
        return TeamIdentity

    def MatchPercentage(self):
        PercentageArray = [0, 0, 0, 0, 0, 0, 0, 0]

        if self.BrokenBot or self.BinStackedHeight < config.MinimumBinHeight and config.absBin or self.AlternatePlatform:
            percentage = 0
        else:
            PercentageArray[0] = self.StackedHeight >= config.heightMin * config.heightValue
            PercentageArray[1] = self.BinStackedHeight >= config.binMin * config.binValue
            PercentageArray[2] = self.Autonomous * config.autonValue
            PercentageArray[4] = config.bankrobCheck * self.StealBins * config.bankrobValue
            PercentageArray[5] = config.throwNoodleCheck * self.ThrowNoodles * config.throwNoodleValue
            PercentageArray[6] = config.noodleInBinCheck * self.FillBin * config.noodleInBinValue
            PercentageArray[7] = self.ChuteUsed * config.chuteValue

            teamScore = sum(PercentageArray)
            maxScore = config.heightValue + config.binValue + config.stacksValue + config.litterValue + config.bankrobValue
            percentage = float(teamScore) / float(maxScore) * 100

        return percentage

def main():
    testlist = ['5431',
                'Titan Robotics',
                '0',
                '',
                '6',
                '0',
                'True',
                'False',
                'False',
                'True',
                'False',
                'False',
                'False',
                '0',
                'True',
                'False'
                ]

    team = Team(testlist)
    print team.TeamIdentity()
    print team.MatchPercentage()

if __name__ == '__main__':
    main()
