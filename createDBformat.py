from os import chdir
from time import sleep
import sqlite3

import config

chdir(config.textDir)
db = sqlite3.connect("scout.db")
cursor = db.cursor()

sqlstuff = '''CREATE TABLE teams 
                (teamname TEXT,
                teamnum INT,
                groups CHAR(1),
                percentage INT);'''


cursor.execute(sqlstuff)

db.commit