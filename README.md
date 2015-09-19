# FRC-Scrutor
Titan Robotics (FRC 5431) scouting analyzation tool for Recycling Rush 2015

You should look through the previous commits to see just how terrible a programmer I was. That's also the reason for 200 commits for a tiny program that should've been written in one sitting.

### Usage
#### Preparing text files
A list should be written in a text file in this format.

```
TeamList[0] = (int) Team Number

TeamList[1] = (str) Team Name

TeamList[2] = (int) Match number

TeamList[3] = (str) Notes about the match or bot 

TeamList[4] = (int) How high they can stack totes 

TeamList[5] = (int) How high they can stack a bin on their own totes  

TeamList[6] = (bool) If the chute is used 

TeamList[7] = (bool) If the bot broke during the match 

TeamList[8] = (bool) If the bot needs to user an alternate scoring platform. ie, right chute but left scoring platform 

TeamList[9] = (bool) If the bot can steal bins

TeamList[10] = (bool) If the human player throwns litter

TeamList[11] = (bool) If the human player fills a bin with recycling 

TeamList[12] = (bool) If the bot can do coopertition

TeamList[13] = (int) How high the bot can place bins on others tote stacks  

TeamList[14] = (bool) If they do autonomous  

TeamList[15] = (bool) If the bot can do autonomous tote set
```

All of the indexes must be contained in a string, so if you want TeamList[14] to be a boolean true, it must be "True"

#### Config file

The config file allows you to change how much a certain change contributes to the final percentage. High value = High contribution.

Before you run the program, go into the config and change the textDir to the directory where you are storing all of the text files that contain the lists

#### Running

To run, just run run.py. It'll give you updates on what it's currently doing.

To retreive the data, just go into the directory that run is located at, and look at finalrankings.csv



