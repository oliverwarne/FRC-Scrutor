from ast import literal_eval
from glob import glob
from os import chdir
from time import sleep

import csv
import sys


#writer = csv.writer(sys.stdout)

import IO
import config

chdir(config.textDir)

while True: 
    for file in glob("*.txt"): #glob scans a directory and i use it to return all the file names
        scanned = open("scanned.cfg","a+") # this file is written to when it has checked 
        csvfile = open('test.csv','a+')
        writer = csv.writer(csvfile)
        with open(file,"r") as f:
            for line in f:
                line = literal_eval(line) #hackity hack hack hack. at least it's more secure than eval
                if f.name not in scanned.read():
                    scanned.write(f.name + "\n")
                    rowToWrite = [IO.teamPercentage(line),line[0],line[1],]
                    print rowToWrite
                    writer.writerow(rowToWrite)
                else:
                    print "This has already been analyzed!"
        scanned.close
        csvfile.close
          
        sleep(2)