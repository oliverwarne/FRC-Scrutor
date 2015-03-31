import analyzation
import filecreate
import os
import glob
import time
import ast
import string
os.chdir("davids-thing/TestTexts/")

def CreateArray(line):
    # this function creates an array that has team num,name, and percentage score. 
    # can't really be used outside of this specific usage case (inside the for loop
    # below)
    finalarray = []
    lineperc = analyzation.PercentageCheckAbsolute(line)
    finalarray.append(str(lineperc))
    splitname = f.name.split("-")
    splitname = splitname[0] + " " + splitname[1]
    finalarray.append(splitname)
    finalarray = ' '.join(finalarray)
    return finalarray

while True: 
    for file in glob.glob("*.txt"): #glob.glob scans a directory and i use it to return all the file names
        scanned = open("scanned.cfg","a+") # this file is written to when it has checked 
        finalpercentage = open("percentage.file","a+") # this file it to be written to with the final percentage
        with open(file,"r") as f:
            for line in f:
                line = ast.literal_eval(line) #hackity hack hack hack. at least it's more secure that eval()
                if f.name in scanned.read():
                    print "This has already been analyzed!"
                else:
                    scanned.write(f.name + "\n")
                    finalpercentage.write(CreateArray(line) + "\n")
    time.sleep(20)


scanned.close

finalpercentage.close

        

    