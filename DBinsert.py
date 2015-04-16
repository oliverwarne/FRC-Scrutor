from os import chdir
from time import sleep
import sqlite3
from IO import teamPercentage

import config

example = ['5431','TitanRobotics','30','6','0','3','False','True','False','False','False','Good Team','B']

chdir(config.textDir)
conn = sqlite3.connect("scout.db")
c = conn.cursor()

sqlinsert = [example[1], example[0], example[12], teamPercentage(example)]

c.execute('insert into teams values (?,?,?,?)' , sqlinsert)
print "inserted!"

