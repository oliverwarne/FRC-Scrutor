from ast import literal_eval
import analyze
import config


def teamIdentity(file):
    with open(file) as f:
        teamIdentity = f.name.split("-")
        teamIdentity = teamIdentity[0] + " " + teamIdentity[1] #gets team name + num
    return teamIdentity

def teamPercentage(team):
    # Array Creation

    percentageArray = [0,0,0,0,0,0,0,0]
    if literal_eval(team[6]) or (literal_eval(team[3]) < config.absoluteMinimumBin) or literal_eval(team[7]):
        percentage = 0
    else:
        percentageArray[0] = ((literal_eval(team[2])) >= (config.heightMin)) * (config.heightValue)
        percentageArray[1] = ((literal_eval(team[3])) >= (config.binMin)) * (config.binValue)
        # percentageArray[2] = (literal_eval(team[5]) >= config.stacksMin) * config.stacksValue
        percentageArray[2] = (literal_eval(team[12])) * config.autonValue
        percentageArray[3] = (literal_eval(team[13])) * config.toteAutonValue
        #TODO : GET APP TO WORK AND ADD HOW MANY STACKS THEY DID!!!!
        percentageArray[4] = analyze.boolPassFail(config.bankrobCheck, literal_eval(team[8])) * config.bankrobValue
        #SECTION BELOW WAS DONE AS FAVOR BY USAID
        percentageArray[5] = analyze.boolPassFail(config.throwNoodleCheck, literal_eval(team[10])) * config.throwNoodleValue
        percentageArray[6] = analyze.boolPassFail(config.noodleInBinCheck, literal_eval(team[11])) * config.noodleInBinValue
        percentageArray[7] = (literal_eval(team[6])) * config.chuteValue
        #SECTION ABOVE WAS DONE AS FAVOR BY USAID
        
        teamScore = sum(percentageArray)
        if isinstance(literal_eval(team[9]),int):
            if literal_eval(team[9]) <= 6:
                teamScore = teamScore+(literal_eval(team[9]) *config.stacksValue)
        maxScore = config.heightValue + config.binValue + config.stacksValue + config.litterValue + config.bankrobValue
        percentage = float(teamScore) / float(maxScore) * 100
    
    # Percentage Creation
    return percentage

test = ['5431','Titan2 Robotics','6','0','True','30','False','False','False','','False','False','False','0','True','False']

print teamPercentage(test)
