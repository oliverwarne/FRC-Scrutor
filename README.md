# Scrutor
Hello! This is FRC Titan Robotics 5431 backend scouting analyzation code. It's pretty close to done.

If you want to use this, don't. The earliest it'll be complete and usable by somebody who isn't looking at the code is 4/14/15.

## How To Use

##### Input 

Our analyzation program can accept any text file in the format below, so you can easily create your own tool. It does have a bit of leniency in the sense that it if you were to pass [2] as a number in a string, it would turn it into a integer. It doesn't have any exception catching, so it'll just crash if you pass it a really weird input.

```
Array[0] = TeamNum (string)
Array[1] = TeamName (string)
Array[2] = The stack height of totes that they can reliably stack (int)
Array[3] = The height of totes on which they can reliably place a bin (int)
Array[4] = If they use the chute (bool)
Array[5] = Match number (string)
Array[6] = If the robot broke during this match (bool)
Array[7] = If the robot can ONLY use an alternate scoring platform (bool) 
Array[8] = If the robot can steal bins from the landfill (bool)
Array[9] = Other notes regarding how the robot functions (string)
Array[10] = If they throw noodles
Array[11] = If they put a noodle in a recycling container
Array[12] = If they did coopertition
Array[13] = On how many OTHER TEAMS totes can they place a bin? 0 being they can't (int)
Array[14] = Do they do autonomous? (bool) 
Array[15] = Do they do autonomous tote set? (bool)
```
There is no built in gui for making them.

To configure your analyzation settings, open up config.py and mess around with those.

#####  Output

Before you can get started, you have to go into config.py and point os.chdir() to where you have the text files stored.

To actually begin the analyzation, just run scan.py. It will spit out a percentage of how well the team matches up, and teams number, and the teams name into a csv file.







