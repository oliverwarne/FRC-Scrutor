# Ugly-Scouting-Code
Hello! This is FRC Titan Robotics 5431 scouting code. When it's done, it *should* have 2 modes. 11st is the input where you either type in a teams stats (formatted how we do it), and then the 2nd mode where it analyzes the data and gives the teams a ranking. 

If you want to use this, don't. The earliest it'll be complete and usable by somebody who isn't looking at the code is 4/22/15.

## How To Use

##### Input 

Our analyzation program can accept any text file in the format below, so you can easily create your own tool. It does have a bit of leniency in the sense that it if you were to pass [2] as a number in a string, it would turn it into a integer. It doesn't have any exception catching, so it'll just crash if you pass it a really weird input.
```
Array[0] = TeamNum (string)
Array[1] = TeamName (string)
Array[2] = The stack height of totes that they can reliably stack (int)
Array[3] = The height of totes on which they can reliably place a bin (int)
Array[4] = If they use litter in any way (bool)
Array[5] = If they use the chute (bool)
Array[6] = Match number (string
Array[7] = If the robot broke during this match (bool)
```

To create an array on windows, run input_gui.py. It writes to the same directory that the input_gui.py is.

To configure your analyzation settings, open up config.py and mess around with those. Everything is commeneted so you should be able to understand what's happening.

#####  Output

Before you can get started, you have to go into scan.py and change os.chdir() to where you have the text files stored.

To actually begin the analyzation, just run scan.py. It will spit out the score, teamname, and teamnum into percentage.file in a loop, so you can leave it running and have the directory filled by another program.







