# Scrutor
Hello! This is FRC Titan Robotics 5431 backend scouting analyzation code. It's pretty close to done.

If you want to use this, don't. The earliest it'll be complete and usable by somebody who isn't looking at the code is 4/14/15.

## How To Use

##### Input 

Our analyzation program can accept any text file in the format below, so you can easily create your own tool. It does have a bit of leniency in the sense that it if you were to pass [2] as a number in a string, it would turn it into a integer. It doesn't have any exception catching, so it'll just crash if you pass it a really weird input.

```
Array[0] = TeamNum (string)
Array[1] = TeamName (string)
Array[2] = Match number (string)
Array[3] = The stack height of totes that they can reliably stack (int)
Array[4] = The height of totes on which they can reliably place a bin (int)
Array[5] = If they use litter in any way (bool)
Array[6] = If they use the chute (bool)
Array[7] = If the robot broke during this match (bool)
Array[8] = If the robot can ONLY use an alternate scoring platform (bool) 
Array[9] = If the robot can steal bins from the landfill (bool)
Array[10] = Other notes regarding how the robot functions (string)
Array[11] = On how many OTHER TEAMS totes can they place a bin? 0 being they can't (int)
Array[12] = Do they do autonomous? (bool) 
Array[13] = Do they do autonomous tote set? (bool)
Array[14] =
```
There is no built in gui for making them.

To configure your analyzation settings, open up config.py and mess around with those. Everything is commeneted so you should be able to understand what's happening.

#####  Output

Before you can get started, you have to go into scan.py and change os.chdir() to where you have the text files stored.

To actually begin the analyzation, just run scan.py. It will spit out the score, teamname, and teamnum into percentage.file in a loop, so you can leave it running and have the directory filled by another program.







