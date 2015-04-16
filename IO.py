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
    if literal_eval(team[8]) or (literal_eval(team[4]) < config.absoluteMinimumBin):
        percentage = 0
    else:
        percentageArray[0] = (literal_eval(team[2]) >= config.heightMin) * config.heightValue  #Height TODO: GET ACTUAL INDEX POSITIONS
        percentageArray[1] = (literal_eval(team[3]) >= config.binMin) * config.binValue
        # TODO : GET ON DAVIDS ASS TO DO THIS 
        percentageArray[2] = (literal_eval(team[5]) >= config.stacksMin) * config.stacksValue
        percentageArray[3] = analyze.boolPassFail(config.litterCheck,literal_eval(team[6])) * config.litterValue
        percentageArray[4] = analyze.boolPassFail(config.bankrobCheck,literal_eval(team[10])) * config.bankrobValue
        
        #SECTION BELOW WAS DONE AS FAVOR BY USAID
        percentageArray[5] = analyze.boolPassFail(config.throwNoodleCheck, literal_eval(team[11])) * config.throwNoodleValue
        percentageArray[6] = analyze.boolPassFail(config.noodleInBinCheck, literal_eval(team[12])) * config.noodleInBinValue
        percentageArray[7] = analyze.boolPassFail(config.coopertitionCheck, literal_eval(team[13])) * config.coopertitionValue
        #SECTION ABOVE WAS DONE AS FAVOR BY USAID
        
        
        #TODO: Description of autonomus program 
        
        teamScore = sum(percentageArray)
        maxScore = config.heightValue + config.binValue + config.stacksValue + config.litterValue + config.bankrobValue
        percentage = float(teamScore) / float(maxScore) * 100
    
    # Percentage Creation
    return percentage
