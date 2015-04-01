import config
from analyzation import PercentageCheckAbsolute
from os import chdir
from glob import glob
from time import sleep
from ast import literal_eval

chdir(config.dirScouted)

def CreateArray(line):
    # this function creates an array that has team num,name, and percentage score. 
    # can't really be used outside of this specific usage case (inside the for loop
    # below)
    finalarray = []
    lineperc = PercentageCheckAbsolute(line)
    finalarray.append(str(lineperc))
    splitname = f.name.split("-")
    splitname = splitname[0] + " " + splitname[1]
    finalarray.append(splitname)
    finalarray = ' '.join(finalarray)
    return finalarray

while True: 
    for file in glob("*.txt"): #glob scans a directory and i use it to return all the file names
        scanned = open("scanned.cfg","a+") # this file is written to when it has checked 
        finalpercentage = open("percentage.file","a+") # this file it to be written to with the final percentage
        with open(file,"r") as f:
            for line in f:
                line = literal_eval(line) #hackity hack hack hack. at least it's more secure than eval()
                if f.name in scanned.read():
                    print "This has already been analyzed!"
                else:
                    scanned.write(f.name + "\n")
                    finalpercentage.write(CreateArray(line) + "\n")
    sleep(20)


scanned.close

finalpercentage.close

        

    