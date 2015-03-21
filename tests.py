import main
import listmanagment

def Create0InitalizedArray():
    EmptyArray = []
    for n in range(0,7):
        EmptyArray.append(0)
    return EmptyArray
    
EmptyArray = Create0InitalizedArray()


print EmptyArray
listmanagment.InputListIntoScoutedArray("5431","Titan Robotics",6,0,"NotPass","DoesPass",30,EmptyArray)
print EmptyArray
