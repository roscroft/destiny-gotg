import os
import sqlite3

def checkDB():
    return os.path.isfile(os.environ['DB_PATH'])

def buildBD():
    print("GOT THAT SHIT")
