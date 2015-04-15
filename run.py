from ast import literal_eval
from glob import glob
from os import chdir
from time import sleep

import IO
import config

chdir(config.textDir)


while True: 
    for file in glob("*.txt"): #glob scans a directory and i use it to return all the file names
        scanned = open("scanned.cfg","a+") # this file is written to when it has checked 
        finalpercentage = open("percentage.file","a+") # this file it to be written to with the final percentage
        with open(file,"r") as f:
            for line in f:
                line = literal_eval(line) #hackity hack hack hack. at least it's more secure than eval
                if f.name not in scanned.read():
                    scanned.write(f.name + "\n")
                    finalpercentage.write(str(IO.teamPercentage(line)) + " " + str(line[0]) + "-" + str(line[1]) + "\n")
                else:
                    print "This has already been analyzed!"
        scanned.close
        finalpercentage.close
    
          
        sleep(2)