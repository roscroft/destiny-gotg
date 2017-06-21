import sqlite3 as lite
import sys
#Manages single user stat requests

def singleStatReq(req, author):
    req = req.toLower()
    con = lite.connect('../Leaderboard/guardian.db')
    with con:
        cur = con.cursor()
        
        if req == 'pvp kd':
            cur.execute("SELECT killDeathRatio FROM PvPTotal")
            rows = cur.fetchall()
            return author+", your k/d ratio in PvP is: "+str(rows[0][0])
        elif req == 'pvp kills total':
            cur.execute("SELECT kills FROM PvPTotal")
            rows = cur.fetchall()
            return author+", your total number of kills in PvP is: "+str(rows[0][0])
        elif req == 'pvp kills average':
            cur.execute("SELECT kills FROM PvPPGA")
            rows = cur.fetchall()
            return author+", your average number of kills in PvP is: "+str(rows[0][0])
