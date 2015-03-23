__name__ = "listcreate"

# Testing stuff
Titan_Array = ["5431","Titan Robotics",6,0,False,True,30]
GlobalArrayName = [" "]
NewArray = [0,0,0,0,0,0,0]
NewArray2 = []
def Create0InitArray():
    EmptyArray = []
    for i in range(0,7):
        EmptyArray.append(0)
    return EmptyArray

### CUSTOMIZATION END ###

### LIST MANAGMENT BEGIN ###
def InputListIntoScoutedArray(TeamNum,TeamName,Totes,BinOnTotes,Litter,Chute,MatchNum,Scouted_Array):
    InputArray = [TeamNum,TeamName,Totes,BinOnTotes,Litter,Chute,MatchNum]
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
        
def ParseBoolInput(TeamBool,Scouted_Array,DataType):
    # Clean the bool input, assign it to a variable, insert it into the list. NOT ABSOLUTE
    ### THIS NEEDS TO BE PUT IN THE REAL ORDER!!!! IT WILL BREAK IF ITS NOT!
    DataType = ParseDataType(DataType)
    print DataType
    if isinstance(TeamBool,bool):
        Scouted_Array[DataType] = TeamBool
    else:
        TeamBool = bool(TeamBool)
        Scouted_Array[DataType] = TeamBool
    return Scouted_Array
            
def ParseIntegerInput(TeamInt,Scouted_Array,DataType):
    # TeamInt is any number that needs to parsed and put into the list.
    # This snippet actually inserts the TeamInt at the DataType index pos.
    # Datatype is, in reality, the index position of list. Should be passed to
    # this function via the ParseDataType function
    DataType = ParseDataType(DataType)
    if isinstance(TeamInt,int):
        Scouted_Array[DataType] = TeamInt
    return Scouted_Array            

def ParseDataType(DataType):
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
