import os
import sqlite3
import initdb
import manifest
import builddb

def checkDB():
    """Check to see if a database exists"""
    return os.path.isfile(os.environ['DBPATH'])

def initDB():
    """Sets up the tables for the database"""
    pass

def checkManifest():
    """Check to see if manifest file exists"""
    return os.path.isfile(os.environ['MANIFEST_CONTENT'])

def getManifest():
    """Pulls the requested definitions into the manifest database"""
    manifest.getManifest()

def buildDB():
    """Main function to build the full database"""
    builddb.buildDB()
