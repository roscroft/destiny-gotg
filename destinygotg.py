#!/usr/bin/python3.6
"""This is the controller for the entire database and bot project."""
import os
import sys
import json
import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import model

# Create the application-level engine and SESSIONMaker objects
# Add echo=True to below line for SQL logging
CONFIG = "config.json"

def load_vars():
    """Loads in environment variables."""
    with open(CONFIG, 'r') as config_file:
        config = json.load(config_file)
        for value in config:
            os.environ[value] = str(config[value])

def write_vars(key, value):
    """Allows changing of environment variables."""
    with open(CONFIG, 'r+') as config_file:
        config = json.load(config_file)
    config[key] = value
    with open(CONFIG, 'w+') as config_file:
        json.dump(config, config_file)
    load_vars()

load_vars()

ENGINE = create_engine(f"sqlite:///{os.environ['APP_PATH']}/{os.environ['DB_NAME']}")
SESSION = sessionmaker(bind=ENGINE)

def main():
    """Run the application"""
    parser = argparse.ArgumentParser(
        description="Build a Destiny clan database and run the Discord bot.")
    parser.add_argument(
        "--path", help="Specify a path for the database and configuration files")
    parser.add_argument(
        "--name", help="Specify a database name")
    parser.add_argument(
        "-n", "--nodisc", help="Do not run the bot automatically", action="store_true")
    parser.add_argument(
        "-u", "--update", help="Update the entire database", action="store_true")
    parser.add_argument("-b", "--bungie", help="Build the Bungie table", action="store_true")
    parser.add_argument("-a", "--account", help="Build the Account table", action="store_true")
    parser.add_argument("-c", "--character", help="Build the Character table", action="store_true")
    parser.add_argument(
        "-s", "--stats", help="Build the CharacterTotalStats table", action="store_true")
    parser.add_argument(
        "-k", "--weapons", help="Build the CharacterWeaponStats table", action="store_true")
    parser.add_argument(
        "-e", "--exotics", help="Build the CharacterUniqueWeaponStats table", action="store_true")
    parser.add_argument(
        "-m", "--medals", help="Build the CharacterMedalStats table", action="store_true")
    parser.add_argument(
        "-f", "--account2", help="Finish building the Account table", action="store_true")
    parser.add_argument(
        "-t", "--accountstats", help="Build the AccountTotalStats and AccountWeaponStats tables",
        action="store_true")
    parser.add_argument("-r", "--refs", help="Build the Reference tables", action="store_true")
    parser.add_argument(
        "-l", "--clean", help="Delete the database and completely rebuild", action="store_true")
    parser.add_argument("-w", "--write", help="Write JSON output files", action="store_true")
    args = parser.parse_args()
    if args.path is not None:
        write_vars("APP_PATH", args.path)
    if args.name is not None:
        write_vars("DB_NAME", args.name)
    if args.write:
        write_vars("WRITE_FILES", int(args.write))

    init_opts = {"clean": args.clean}

    build_opts = {"bungie": args.bungie, "account": args.account, "character": args.character,
                  "stats": args.stats, "weapons": args.weapons, "exotics": args.exotics,
                  "medals": args.medals, "account2": args.account2,
                  "accountstats": args.accountstats, "refs": args.refs, "update": args.update,
                  "clean": args.clean}

    # Ensure that the program is running on python 3.6+
    if not verify_python_version():
        print("This app requires python 3.6 or greater!")
        return
    # Make sure the APP_PATH directory exists
    # set_app_path()

    # Ensure a correct config file exists
    if not config_exists():
        generate_config()

    # Load the config values into environment vars
    load_vars()

    if not model.check_manifest():
        model.get_manifest()

    model.init_db(init_opts)

    model.build_db(build_opts)

    if not args.nodisc:
        model.run_discord()

# def set_app_path():
#     """Ensures the APP_PATH dir exists"""
#     if not os.path.isdir(APP_PATH):
#         os.mkdir(APP_PATH)

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
    apikey = input("Please enter your Bungie API Key: ")
    clanid = input("Please enter your Clan ID: ")
    disc_apikey = input("Please enter your Discord API Key: ")
    db_name = input("Please enter a filename for the database: ")
    config_dict = {"BUNGIE_APIKEY": apikey, "BUNGIE_CLANID": clanid, "DISCORD_APIKEY": disc_apikey,
                   "DB_NAME": db_name, "MANIFEST_NAME": "manifest.content"}
    with open(CONFIG, 'w+') as config_file:
        json.dump(config_dict, config_file)

def config_exists():
    """Check if there are any missing fields, or if the file doesn't exist"""
    if os.path.exists(f"{CONFIG}"):
        return True
    print("No config file")
    return False

def run_flask():
    """Runs the Flask portion of the project. Currently useless."""
    os.environ['FLASK_APP'] = "views/flask/app.py"
    os.system("flask run --host=0.0.0.0")

if __name__ == "__main__":
    main()
