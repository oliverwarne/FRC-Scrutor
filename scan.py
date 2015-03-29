import analyzation
import os
import glob
import time
import array
from ast import literal_eval
os.chdir("TestTexts/")
scanned = open("scanned.txt","a")
for file in glob.glob("*.txt"):
    f = open(file)
    for line in f:
        line = line.split[1]
        print analyzation.BoolArrayIntoTeamScore(line)
        
        
