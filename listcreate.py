__name__ = "listcreate"

### LIST CREATION BEGIN ###

def InputListIntoScoutedArray(TeamNum,TeamName,Totes,BinOnTotes,Litter,Chute,MatchNum,Scouted_Array):
    # You pass this function the array that you want to fill up, and all the ***CLEANED*** data that
    # you want. This WILL likely break if you pass it dirty data. It does have a little bit of cleaning
    # where it tries to turn the thing that its passed into an int/str/bool, but it's still going to 
    # mess up if you try to pass the bool a string that isn't a "True"/"False" or something similar 
    # to that. 
    # This is pretty ugly, and you could improve by having it dynamically detect 
    # what type of data is input, and then use the appropriate input parsing.
    ParseStringInput(TeamNum,Scouted_Array,"TeamNum")
    ParseStringInput(TeamName,Scouted_Array,"TeamName")
    ParseIntegerInput(Totes,Scouted_Array,"Totes")
    ParseIntegerInput(BinOnTotes,Scouted_Array,"BinOnTotes")
    ParseBoolInput(Litter,Scouted_Array,"Litter")
    ParseBoolInput(Chute,Scouted_Array,"Chute")
    ParseIntegerInput(MatchNum,Scouted_Array,"MatchNum")
    return Scouted_Array
    
def ParseStringInput(TeamString,Scouted_Array,DataType):
    # Clean the string input, assign it to a variable, insert it into the list. NOT ABSOLUTE
    ### THIS NEEDS TO BE PUT IN THE REAL ORDER!!!! IT WILL BREAK IF ITS NOT!
    DataType = ParseDataType(DataType)
    if isinstance(TeamString,str):
        Scouted_Array[DataType] = TeamString
    else:
        TeamString = str(TeamString)
        Scouted_Array[DataType] = TeamString
    return Scouted_Array

def ParseIntegerInput(TeamInt,Scouted_Array,DataType):
    # TeamInt is any number that needs to parsed and put into the list.
    # This snippet actually inserts the TeamInt at the DataType index pos.
    # Datatype is, in reality, the index position of list. Should be passed to
    # this function via the ParseDataType function
    DataType = ParseDataType(DataType)
    if isinstance(TeamInt,int):
        Scouted_Array[DataType] = TeamInt
    else:
        TeamInt = int(TeamInt)
        Scouted_Array[DataType] = TeamInt
    return Scouted_Array  

def ParseBoolInput(TeamBool,Scouted_Array,DataType):
    # Clean the bool input, assign it to a variable, insert it into the list. NOT ABSOLUTE
    ### THIS NEEDS TO BE PUT IN THE REAL ORDER!!!! IT WILL BREAK IF ITS NOT!
    DataType = ParseDataType(DataType)
    if isinstance(TeamBool,bool):
        Scouted_Array[DataType] = TeamBool
    else:
        TeamBool = bool(TeamBool)
        Scouted_Array[DataType] = TeamBool
    return Scouted_Array

def ParseDataType(DataType):
    # This accepts the datatype that you're looking for, and returns the index 
    # of what it should be in the array.
    IndexDict = {
                'TeamNum': 0,
                'TeamName': 1,
                'Totes': 2,
                'BinOnTotes': 3,
                'Litter': 4,
                'Chute': 5,
                'MatchNum': 6
                }
    return IndexDict[DataType]

### LIST CREATION END ###
