from ast import literal_eval
from glob import glob
from os import chdir
from time import sleep

import csv
import sys

import config

chdir("realTexts/")
print "Started Run"
while True: 
    for file in glob("*.txt"):  #glob scans a directory and i use it to return all the file names
        scanned = open('scanned.config', 'a+')  # this file is written to when it has checked
        csvfile = open('rawData.csv', 'a+')
        writer = csv.writer(csvfile)
        with open(file, "r") as f:
            for line in f:
                line = literal_eval(line)  #hackity hack hack hack. at least it's more secure than eval
                if f.name not in scanned.read():
                    scanned.seek(0)
                    try:
                        scanned.write(str(f.name)+"\n")
                    except IOError:
                        print "Error writing to scanned file, WILL NOT SAVE CURRENT DATA"
                    print line
                    writer.writerow(line)
                else:
                    print "This has already been written to the CSV!"
        scanned.close
        csvfile.close
