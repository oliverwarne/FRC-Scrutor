import main
import listcreation
import listinterp


def Create0InitalizedArray():
    EmptyArray = []
    for n in range(0,7):
        EmptyArray.append(0)
    return EmptyArray
    
EmptyArray = Create0InitalizedArray()
EmptyArray2 = Create0InitalizedArray()


print EmptyArray
listcreation.InputListIntoScoutedArray("5431","Titan Robotics",6,0,"False","True",30,EmptyArray)
print EmptyArray

print listinterp.PeekArray(EmptyArray,"TeamChute")
print listinterp.PeekArrayHACK(EmptyArray,"TeamChute")

print type(listinterp.PeekArray(EmptyArray,"TeamChute"))
print type(listinterp.PeekArrayHACK(EmptyArray,"TeamChute"))


