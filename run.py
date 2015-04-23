from ast import literal_eval
from glob import glob
from os import chdir
from time import sleep

import csv
import sys

last = False
current = False

writer = csv.writer(sys.stdout)

import IO
import config

chdir(config.textDir)
print "Started Run"
while True: 
    for file in glob("*.txt"):  #glob scans a directory and i use it to return all the file names
        scanned = open('scanned.config', 'a+')  # this file is written to when it has checked
        csvfile = open('finalrankings.csv', 'a+')
        writer = csv.writer(csvfile)
        with open(file, "r") as f:
            for line in f:
                line = literal_eval(line)  #hackity hack hack hack. at least it's more secure than eval
                if f.name not in scanned.read():
                    current = True
                    try:
                        scanned.write(str(f.name)+"\n")
                    except IOError:
                        print "Error writing to scanned file, WILL NOT SAVE CURRENT DATA"
                    rowToWrite = [IO.teamPercentage(line), line[0], line[1]]
                    print str(rowToWrite)
                    writer.writerow(rowToWrite)
                else:
                    current = False
                    if last and not current:
                        print "This has already been analyzed!"
            last = current
        scanned.close
        csvfile.close
        sleep(5)
