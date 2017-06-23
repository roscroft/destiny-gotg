import sqlite3 as lite

def registerUser(author):
    authorTup = (author,)
    con = lite.connect('../Leaderboard/guardians.db')
    output = ""
    with con:
        cur = con.cursor()

        cur.execute("SELECT EXISTS(SELECT Name FROM Discord WHERE Name=?",(author,)

        if cur.fetchone():
            cur.execute("UPDATE Discord SET discName=? WHERE Name=?",(author, author))
            output = "Successfully registered as: " + author

        else:
            output = author+", please enter your PSN display name."
            cur.execute("UPDATE Discord SET discName=?
