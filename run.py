from team import team
from config import textDir
from ast import literal_eval
from glob import glob
from os import chdir
from time import sleep

import csv
import sys

last = False
current = False

writer = csv.writer(sys.stdout)

chdir(textDir)
print "Started Run"
while True:
    for file in glob("*.txt"):  # glob scans a directory and i use it to return all the file names
        scanned = open('scanned.config', 'a+')  # this file is written to when it has checked
        csvfile = open('finalrankings.csv', 'a+')
        writer = csv.writer(csvfile)
        with open(file, "r") as f:
            for line in f:
                Team = team(literal_eval(line))  # hackity hack hack hack. at least it's more secure than eval
                if Team.TeamIdentity() not in scanned.read():
                    try:
                        scanned.seek(0)
                        scanned.write(Team.TeamIdentity() + '\n')
                    except IOError:
                        print "Error writing to scanned file, WILL NOT SAVE CURRENT DATA"
                        continue
                    rowToWrite = [Team.MatchPercentage(), Team.TeamIdentity()]
                    print str(rowToWrite)
                    writer.writerow(rowToWrite)
                else:
                    print "This has already been analyzed!"
        scanned.close
        csvfile.close
        sleep(.1)