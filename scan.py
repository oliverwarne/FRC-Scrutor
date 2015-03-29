import analyzation
import os
import glob
import time
os.chdir("TestTexts/")
config = open("config.txt","a")
for file in glob.glob("*.txt"):
    f = open(file)
    for line in f:
        print line
        print analyzation.BoolArrayIntoTeamScore(line)
