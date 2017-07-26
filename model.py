import os
import sqlite3
import manifest
import builddb

def checkDB():
    """Check to see if a database exists"""
    return os.path.isfile(os.environ['DBPATH'])

def initDB():
    """Sets up the tables for the database"""
    import initdb

def checkManifest():
    """Check to see if manifest file exists"""
    return os.path.isfile(os.environ['MANIFEST_CONTENT'])

def getManifest():
    """Pulls the requested definitions into the manifest database"""
    manifest.getManifest()

def buildDB():
    """Main function to build the full database"""
    print("Am i even called?")
    builddb.buildDB()
