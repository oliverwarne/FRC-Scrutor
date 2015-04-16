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
    percentageArray = [0,0,0,0,0]
    if literal_eval(team[9]) or (literal_eval(team[4]) < config.absoluteMinimumBin):
        percentage = 0
    else:
        percentageArray[0] = (literal_eval(team[3]) >= config.heightMin) * config.heightValue  #Height TODO: GET ACTUAL INDEX POSITIONS
        percentageArray[1] = (literal_eval(team[4]) >= config.binMin) * config.binValue
        # TODO : GET ON DAVIDS ASS TO DO THIS 
        percentageArray[2] = (literal_eval(team[5]) >= config.stacksMin) * config.stacksValue
        percentageArray[3] = analyze.boolPassFail(config.litterCheck,literal_eval(team[6])) * config.litterValue
        percentageArray[4] = analyze.boolPassFail(config.bankrobCheck,literal_eval(team[10])) * config.bankrobValue
        #TODO: Description of autonomus program
        
        teamScore = sum(percentageArray)
        maxScore = config.heightValue + config.binValue + config.stacksValue + config.litterValue + config.bankrobValue
        percentage = float(teamScore) / float(maxScore) * 100
    
    # Percentage Creation
    return percentage