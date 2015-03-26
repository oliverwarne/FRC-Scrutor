import listcreate
import listinterp
import analyzation

def Create0InitalizedArray():
    EmptyArray = []
    for n in range(0,7):
        EmptyArray.append(0)
    return EmptyArray
    
EmptyArray = Create0InitalizedArray()
EmptyArray2 = Create0InitalizedArray()

### LIST CREATE TESTS ###
print "LIST CREATE"
print EmptyArray
listcreate.InputListIntoScoutedArray("5431","Titan Robotics",6,0,False,True,30,EmptyArray)
# Should return ["5431","Titan Robotics",6,0,False,True,30,EmptyArray]
print EmptyArray

#### LIST INTERP TEST ###
print "LIST INTERP"
print listinterp.PeekArrayTest(EmptyArray,"TeamChute")
# Should return True
print listinterp.PeekArrayTest(EmptyArray2,"TeamChute")
# Should return 0

### ANALYZATION TESTS ###
print "ANALYZATION"
print analyzation.PercentageCheckAbsolute(EmptyArray)
# TODO : Figure out how to write a test for this
