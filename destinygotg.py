#!/usr/bin/python3.6
import os
import sys
import model
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create the application-level engine and SessionMaker objects
# Add echo=True to below line for SQL logging
APP_PATH = "/etc/destinygotg"
DBPATH = f"{APP_PATH}/guardians2.db"

Engine = create_engine(f"sqlite:///{DBPATH}")#, echo=True)
Session = sessionmaker(bind=Engine)

def main():
    """Run the application"""
    parser = argparse.ArgumentParser(description="Build a Destiny clan database and run the Discord bot.")
    parser.add_argument("--path", help="Specify a path for the database and configuration files")
    parser.add_argument("--name", help="Specify a database name")
    parser.add_argument("--nodisc", help="Do not run the bot automatically", action="store_true")
    parser.add_argument("--update", help="Update the entire database", action="store_true")
    parser.add_argument("--bungie", help="Build the Bungie table, default is whole database", action="store_true")
    parser.add_argument("--account", help="Build the Account table, default is whole database", action="store_true")
    parser.add_argument("--character", help="Build the Character table, default is whole database", action="store_true")
    parser.add_argument("--stats", help="Build the CharacterTotalStats table, default is whole database", action="store_true")
    parser.add_argument("--weapons", help="Build the CharacterWeaponStats table, default is whole database", action="store_true")
    parser.add_argument("--exotics", help="Build the CharacterUniqueWeaponStats table, default is whole database", action="store_true")
    parser.add_argument("--medals", help="Build the CharacterMedalStats table, default is whole database", action="store_true")
    parser.add_argument("--account2", help="Fill the Account table with Character information", action="store_true")
    parser.add_argument("--accountstats", help="Build the AccountTotalStats and AccountWeaponStats tables", action="store_true")
    parser.add_argument("--refs", help="Build the Reference tables", action="store_true")
    parser.add_argument("--clean", help="Delete the database and completely rebuild", action="store_true")
    parser.add_argument("--write", help="Write JSON output files", action="store_true")
    args = parser.parse_args()
    if args.path != "":
        APP_PATH = args.path
    if args.name != "":
        DBPATH = args.name

    init_opts = {"clean": args.clean}

    build_opts = {"bungie": args.bungie, "account": args.account, "character": args.character, "stats": args.stats,
            "weapons": args.weapons, "exotics": args.exotics, "medals": args.medals, "account2": args.account2,
            "accountstats": args.accountstats, "write": args.write, "refs": args.refs, "update": args.update, 
            "clean": args.clean}

    # Ensure that the program is running on python 3.6+
    if not verify_python_version():
        print("This app requires python 3.6 or greater!")
        return
    # Make sure the APP_PATH directory exists
    set_app_path()

    # Ensure a correct config file exists
    if not config_exists():
        generate_config()
    
    # Load the config values into environment vars
    load_config()
    
    if not model.check_manifest():
        model.get_manifest()
    
    model.init_db(init_opts)
    
    model.build_db(build_opts)
    
    if not args.nodisc:
        model.run_discord()

def set_app_path():
    """Ensures the APP_PATH dir exists"""
    if not os.path.isdir(APP_PATH):
        os.mkdir(APP_PATH)

def verify_python_version():
    """Ensure the script is being run in python 3.6"""
    try:
        # use assert to throw an exception if
        # the python version is less than 3.6
        assert sys.version_info >= (3, 6)
        return True
    except AssertionError:
        return False

def generate_config():
    """Generate and store a new config file"""
    # make sure the APP_PATH directory exists
    config = open(f"{APP_PATH}/config", "w+")
    apikey = input("Please enter your Bungie API Key: ")
    clanid = input("Please enter your Clan ID: ")
    disc_apikey = input("Please enter your Discord API Key: ")
    config.write(f"BUNGIE_APIKEY:{apikey}\n")
    config.write(f"BUNGIE_CLANID:{clanid}\n")
    config.write(f"DISCORD_APIKEY:{disc_apikey}\n")
    config.write(f"DBPATH:{DBPATH}\n")
    config.write(f"MANIFEST_CONTENT:{APP_PATH}/manifest.content\n")
    config.close()

def config_exists():
    """Check if there are any missing fields, or if the file doesn't exist"""
    if os.path.exists(f"{APP_PATH}/config"):
        return True
    else:
        print("No config file")
        return False
    #TODO: Implement config file checker to see if it has all fields

def load_config():
    """Load configs from the config file"""
    config = open(f"{APP_PATH}/config", "r").readlines()
    for value in config:
        value = value.strip().split(":")
        os.environ[value[0]] = value[1]

def run_flask():
    os.environ['FLASK_APP'] = "views/flask/app.py"
    os.system("flask run --host=0.0.0.0")

if __name__ == "__main__":
    main()
