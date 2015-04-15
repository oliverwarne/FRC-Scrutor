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
    percentageArray = [0,0,0,0,0,0]
    if bool(team[8]):
        percentage = 0
    else:
        percentageArray[0] = (int(team[2]) >= config.heightMin) * config.heightValue  #Height TODO: GET ACTUAL INDEX POSITIONS
        percentageArray[1] = (int(team[3]) >= config.binMin) * config.binValue
        # TODO : GET ON DAVIDS ASS TO DO THIS percentageArray[2] = (int(team[8]) >= config.stacksMin) * config.stacksValue
        percentageArray[2] = config.stacksValue
        percentageArray[3] = analyze.boolPassFail(config.litterCheck,bool(team[5])) * config.litterValue
        percentageArray[5] = analyze.boolPassFail(config.bankrobCheck,bool(team[9])) * config.bankrobValue
        #TODO: Description of autonomus program
        
        teamScore = sum(percentageArray)
        maxScore = config.heightValue + config.binValue + config.stacksValue + config.litterValue + config.litterValue + config.bankrobValue
        percentage = float(teamScore) / float(maxScore) * 100
    
    # Percentage Creation
    return percentage
