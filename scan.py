import analyzation
import os
import glob
import time
import array
import ast
os.chdir("TestTexts/")
scanned = open("scanned.txt","a")
for file in glob.glob("*.txt"):
    f = open(file)
    for line in f:
        line = eval(line)
        lineperc = analyzation.PercentageCheckAbsolute(line)
        print lineperc