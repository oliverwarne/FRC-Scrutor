import analyzation
import filecreate
import os
import glob
import time
import ast
import string
os.chdir("davids-thing/TestTexts/")

def CreateArray(line):
    finalarray = []
    lineperc = analyzation.PercentageCheckAbsolute(line)
    finalarray.append(str(lineperc))
    splitname = f.name.split("-")
    splitname = splitname[0] + " " + splitname[1]
    finalarray.append(splitname)
    finalarray = ' '.join(finalarray)
    return finalarray

while True:
    for file in glob.glob("*.txt"):
        scanned = open("scanned.cfg","a+")
        finalpercentage = open("percentage.file","a+")
        with open(file,"r") as f:
            for line in f:
                line = ast.literal_eval(line)
                if f.name in scanned.read():
                    print "This has already been analyzed!"
                else:
                    scanned.write(f.name + "\n")
                    finalpercentage.write(CreateArray(line) + "\n")
    time.sleep(2)


scanned.close

finalpercentage.close

        

    